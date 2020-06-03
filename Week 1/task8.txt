import re

pattern = ".*Big Data$"
 
txt = "We love programming with Big Data"
 
x = re.search(pattern,txt)

print(x)