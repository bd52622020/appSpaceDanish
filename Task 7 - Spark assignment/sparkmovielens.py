from pyspark import SparkConf, SparkContext
from functools import reduce
from pyspark.sql.functions import array, col, explode, lit, struct, count, avg, mean
from pyspark.sql import DataFrame
from typing import Iterable 
import pyspark.sql.functions as F

#This is creating a melt function that will allow narrow type transformation
def melt(
        df: DataFrame, 
        id_vars: Iterable[str], value_vars: Iterable[str], 
        var_name: str="Genre", value_name: str="value") -> DataFrame:
    _vars_and_vals = array(*(
        struct(lit(c).alias(var_name), col(c).alias(value_name)) 
        for c in value_vars))

    _tmp = df.withColumn("_vars_and_vals", explode(_vars_and_vals))

    cols = id_vars + [
            col("_vars_and_vals")[x].alias(x) for x in [var_name, value_name]]
    return _tmp.select(*cols)

if __name__ == "__main__":

    #Setting sparkcontext
    conf = SparkConf().setAppName("Movielens")
    sc = SparkContext(conf = conf)

    #Reading the main data file
    df = spark.read.csv("/home/danish/Documents/movielens/data/u.item", sep="|", inferSchema="true", header="False", )
    oldColumns = df.schema.names
    newColumns = ["movie_id", "movie_title", "release_date", "video_release_date", "IMDb_URL", "unknown", "Action",
                  "Adventure", "Animation",
                  "Children's", "Comedy","Crime", "Documentary", "Drama","Fantasy",
                  "Film-Noir" ,"Horror", "Musical","Mystery","Romance", "Sci-Fi",
                  "Thriller", "War", "Western"]

    #Cleaning the main data file
    df = reduce(lambda df, col: df.withColumnRenamed(oldColumns[col], newColumns[col]), range(len(oldColumns)), df)
    columns_to_drop = ["video_release_date" , "IMDb_URL"]
    df = df.drop(*columns_to_drop)

    #Applying melt function to transform it into a narrow type dataframe
    df = melt(df, id_vars=["movie_id", "movie_title", "release_date"], value_vars=["unknown", "Action",
                  "Adventure", "Animation",
                  "Children's", "Comedy","Crime", "Documentary", "Drama","Fantasy",
                  "Film-Noir" ,"Horror", "Musical","Mystery","Romance", "Sci-Fi",
                  "Thriller", "War", "Western"])

    df = df.filter(df.value == 1)

    #moviedata will be the main file
    moviedata = df.drop("value")

    #moviedata grouped by all its genres
    moviedatagroup = moviedata.groupBy('movie_id','movie_title','release_date').agg(F.collect_list("Genre"))

    #creating the ratings dataframe
    ratings = spark.read.csv("/home/danish/Documents/movielens/data/u.data", sep="\t", inferSchema="true", header="False", )
    oldColumn = ratings.schema.names
    newColumn = ["user_id","movie_id","rating","timestamp"]
    ratings1 = reduce(lambda ratings, col2: ratings.withColumnRenamed(oldColumn[col2], newColumn[col2]), range(len(oldColumn)), ratings)
    ratings1 = ratings1.drop("timestamp")

    #this dataframe has the total count of each movie
    ratings2 = ratings1.groupBy('movie_id').count()
    ratings2 = ratings2.drop("user_id")

    #this dataframe has the avg rating for each movie
    datastats = ratings1.groupBy("movie_id").mean("rating").alias("avg")
    datastats = datastats.withColumn("avg(rating)", F.round(datastats["avg(rating)"], 1))

    #This dataframe is created from the joining of the main file and the total count dataframe
    data = moviedatagroup.join(ratings2, on="movie_id", how="inner")
    data = data.sort(col("count").desc())

    #This dataframe is joining the main file with the avg ratings dataframe
    data2 = moviedata.join(ratings2, on="movie_id", how="inner")
    data2 = data2.select(["Genre", "count"])
    data2 = data2.groupBy("Genre").sum("count")

    #This dataframe joins the main file with the ratings dataframe
    dataratings = moviedatagroup.join(ratings1, on="movie_id", how="inner")

    #This filters out any movie that wasn't rated 5
    fiveratings = dataratings.filter(dataratings.rating == 5)

    #This DataFrame joins the main file with the avg rating file
    q5 = moviedata.join(datastats, on="movie_id", how="inner")

    #This Dataframe is reading the users information file and cleaning it
    users = spark.read.csv("/home/danish/Documents/movielens/data/u.user", sep="|", inferSchema="true", header="False", )
    old = users.schema.names
    new = ["user_id","age","gender","occupation","zipcode"]
    users = reduce(lambda users, col3: users.withColumnRenamed(old[col3], new[col3]), range(len(old)), users)

    #This dataframe filters ratings only submitted by students
    q6 = users.filter(users.occupation == "student")
    q6 = q6.select("user_id")

    #This dataframe joins the previous filtered dataframe to the ratings dataframe so only
    #user ids belonging to students remain
    studentratings = ratings1.join(q6, on="user_id", how='left_semi')
    studentratings = studentratings.groupBy('movie_id').count()
    studentratings = studentratings.drop("user_id")

    #This joins the main file with the filteres student dataframe created before
    studentdata = moviedatagroup.join(studentratings, on="movie_id", how="inner")

    #Sorts the student dataframe
    studentdata = studentdata.sort(col("count").desc())

    #This dataframe filters ratings that are 5
    fiveratingsonly = ratings1.filter(ratings1.rating == 5)
    fiveratingsonly = fiveratingsonly.groupBy('movie_id').count()
    fiveratingsonly = fiveratingsonly.drop("user_id")

    #This joins the previously created dataframe with the main file
    fiveratingdata = moviedatagroup.join(fiveratingsonly, on="movie_id", how="inner")

    #This sorts the previous dataframe
    fiveratingdata = fiveratingdata.sort(col("count").desc())

    #creates a dataframe that contains zipcodes and its counts
    users2 = users.groupBy('zipcode').count()
    users2 = users2.sort(col("count").desc())

    #Filters out all ages that are not 20-25
    ages = users.filter(users.age > 19)
    ages = ages.filter(users.age < 26)

    #Join to filter out all ratings that are not from the previous age range selected
    ageratings = ratings1.join(ages, on="user_id", how='left_semi')

    #Cleaning the data
    ageratings = ageratings.groupBy('movie_id').count()
    ageratings = ageratings.drop("user_id")

    #Joining on the main file
    agedata = moviedatagroup.join(ageratings, on="movie_id", how="inner")
    agedata = agedata.sort(col("count").desc())

    #Filters out all movies before 1960
    releasedata = data.filter(data.release_date > 1960)
    releasedata = data.sort(col("release_date"))

    ## Question 1 Print a list of the 10 movies that received the most number of ratings. 

    data.select("movie_title").show(10)

    ## Question 2 
    ## Print a list of the 10 movies that received the most number of ratings, sorted by the number of ratings. 

    data.select("movie_title", "count").show10

    ## Question 3
    ## Print a list of the number of ratings received by each genre. 

    data2.show()

    ## Question 4
    ## Print the oldest movie with a “5” rating. 

    fiveratings.sort(col("release_date")).show(1)

    ## Question 5
    ## Print a list of the genre of the top 10 most rated movies. 

    q5.select("Genre").sort(col("avg(rating)").desc()).show(10)

    ## Question 6 Print the title of the movie that was rated the most by students 

    studentdata.select("movie_title").show(1)

    ## Question 7 
    ## Print the list of movies that received the highest number of “5” rating 

    fiveratingdata.select("movie title").show(10)

    ## Question 8
    ## Print the list of zip codes corresponding to the highest number of users that rated movies. 

    users2.show(10)

    ## Question 9
    ## Find the most rated movie by users in the age group 20 to 25. 

    agedata.show(1)

    ## Question 10
    ## Print the list of movies that were rate after year 1960. 

    releasedata.show(10)