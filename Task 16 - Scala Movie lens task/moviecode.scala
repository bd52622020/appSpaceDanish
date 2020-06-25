package com.spark.danish

import org.apache.spark.SparkContext
import org.apache.spark.SparkConf
import org.apache.log4j._
import org.apache.spark.sql.SQLContext
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._
import org.apache.spark.sql.expressions._
import org.apache.spark.sql.functions.{to_date, to_timestamp}

object moviecode {
  
  def main(args: Array[String]) {
   // Setting Spark Session
    Logger.getLogger("org").setLevel(Level.ERROR)
    val spark = SparkSession
      .builder()
      .appName("Movies")
      .master("local[*]")
      .config("spark.sql.warehouse.dir", "file:///C:/temp") //I don't know what to put in here, but this works so am not going to risk changing
      .getOrCreate()
      import spark.implicits._
      
      // Reading in the u.data file
      val rating = spark.read.format("csv")
      .option("sep" , "\t")
      .option("inferScheme","false")
      .option("header","false")
      .load("/home/danish/Documents/movielens/data/u.data")
      .toDF("user_id", "movie_id", "rating", "timestamp")
    
      // Reading in the u.item file
      val df = spark.read.format("csv")
      .option("sep" , "[|]")
      .option("inferScheme","false")
      .option("header","false")
      .load("/home/danish/Documents/movielens/data/u.item")
      .toDF("movie_id")
      .withColumn("_tmp", split($"movie_id", "[|]"))
      .select(
          $"_tmp".getItem(0).as("movie_id"),
          $"_tmp".getItem(1).as("movie_title"),
          $"_tmp".getItem(2).as("video_release_date"),
          $"_tmp".getItem(5).as("unknown"),
          $"_tmp".getItem(6).as("Action"),
          $"_tmp".getItem(7).as("Adventure"),
          $"_tmp".getItem(8).as("Animation"),
          $"_tmp".getItem(9).as("Childrens"),
          $"_tmp".getItem(10).as("Comedy"),
          $"_tmp".getItem(11).as("Crime"),
          $"_tmp".getItem(12).as("Documentary"),
          $"_tmp".getItem(13).as("Drama"),
          $"_tmp".getItem(14).as("Fantasy"),
          $"_tmp".getItem(15).as("Film_Noir"),
          $"_tmp".getItem(16).as("Horror"),
          $"_tmp".getItem(17).as("Musical"),
          $"_tmp".getItem(18).as("Mystery"),
          $"_tmp".getItem(19).as("Romance"),
          $"_tmp".getItem(20).as("Sci_Fi"),
          $"_tmp".getItem(21).as("Thriller"),
          $"_tmp".getItem(22).as("War"),
          $"_tmp".getItem(23).as("Western")
          )
          
       // changing the date coloumn into an actual date type   
       val df2 = df.withColumn("video_release_date", to_date($"video_release_date", "dd-MMM-yyyy"))
          
       
       
       // Reading in the u.user file
       val users = spark.read.format("csv")
       .option("sep" , "[|]")
       .option("inferScheme","false")
       .option("header","false")
       .load("/home/danish/Documents/movielens/data/u.user")
       .toDF("id")
       .withColumn("_tmp", split($"id", "[|]"))
       .select(
           $"_tmp".getItem(0).as("user_id"),
           $"_tmp".getItem(1).as("age"),
           $"_tmp".getItem(2).as("gender"),
           $"_tmp".getItem(3).as("occupation"),
           $"_tmp".getItem(4).as("zip_code")
          )
       
       // unpivoting or melting the dataframe to get Genre Col   
       val maindata = df2.select($"movie_id",
           $"movie_title",
           $"video_release_date",
           expr("stack(19, 'unknown',unknown,'Action', Action,'Adventure', Adventure,'Animation',Animation,'Childrens',Childrens,'Comedy', Comedy,'Crime', Crime,'Documentary', Documentary,'Drama', Drama,'Fantasy',Fantasy,'Film_Noir', Film_Noir,'Horror', Horror,'Musical', Musical,'Mystery', Mystery,'Romance', Romance,'Sci_Fi', Sci_Fi,'Thriller', Thriller, 'War', War, 'Western', Western) as (Genre, value)"))
           .where("value == 1")
           .drop("value")
       
       // Some various rdds neaded for the questions
       val moviedatagroup = maindata.groupBy("movie_id","movie_title","video_release_date").agg(collect_list("Genre"))
       
       val ratingscounts = rating.groupBy("movie_id").count().drop("user_id")
       
       val q1 = moviedatagroup.join(ratingscounts, Seq("movie_id"),"inner").sort(desc("count"))
       
       val q3 = maindata.join(ratingscounts, Seq("movie_id"),"inner").sort(desc("count"))

       println("Question 1")
       // Question 1. Print a list of the 10 movies that received the most number of ratings, sorted by the number of ratings.
       q1.select("movie_title").take(10).foreach(println)
       
       println("Question 2")
       // Question 2. Print a list of the 10 movies that received the most number of ratings. 
       q1.select("movie_title" , "count").show(10)
       
       println("Question 3")
        // Question 3. Print a list of the number of ratings received by each genre.  
       q3.groupBy("Genre").sum("count").sort(desc("sum(count)")).collect().foreach(println)
       
       println("Question 4")
       // Question 4. Print the oldest movie with a “5” rating. 
       moviedatagroup.join(rating.filter($"rating" === "5").select("movie_id"), Seq("movie_id"),"leftsemi")
       .sort(asc("video_release_date")).na.drop().select("movie_title").take(1).foreach(println)
       
       println("Question 5")
       // Question 5. Print a list of the genre of the top 10 most rated movies.
       q3.select($"Genre").rdd.map(r => r(0)).take(10).distinct.foreach(println)
       
       println("Question 6")
       // Question 6. Print the title of the movie that was rated the most by students 
       moviedatagroup.join(rating.join(users.filter($"occupation" === "student").select($"user_id"), Seq("user_id"),"leftsemi")
       .groupBy("movie_id").count(), Seq("movie_id"),"inner").sort(desc("count")).select($"movie_title").take(1).foreach(println)
 
       println("Question 7")
       // Question 7. Print the list of movies that received the highest number of “5” rating 
       moviedatagroup.join(rating.filter($"rating" === "5").select("movie_id").groupBy("movie_id").count(), Seq("movie_id"),"inner")
       .sort(desc("count")).select($"movie_title").take(10).foreach(println)
  
       println("Question 8")
       // Question 8. Print the list of zip codes corresponding to the highest number of users that rated movies.
       users.groupBy("zip_code").count().sort(desc("count")).select("zip_code").take(5).foreach(println)

       println("Question 9")
       // Question 9. Find the most rated movie by users in the age group 20 to 25. 
       moviedatagroup.join(rating.join(users.filter($"age" >= "20" && $"age" <= "25").select($"user_id"), Seq("user_id"),"leftsemi")
       .groupBy("movie_id").count(), Seq("movie_id"),"inner").sort(desc("count")).select($"movie_title").take(1).foreach(println)
       
       println("Question 10")
       // Question 10. Print the list of movies that were rate after year 1960. 
        q1.filter(year($"video_release_date").geq(lit(1960))).select("movie_title").take(10).foreach(println)

  } 
  
}