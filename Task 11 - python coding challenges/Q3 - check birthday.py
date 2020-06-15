#!/usr/bin/env python


birthdays = {"Person1" : "16/12/1992" , "Person2" : "07/07/1998" , "Person3" : "01/02/1983","Person4" : "07/01/1962", "Person5" : "11/02/1998" ,"Person6" : "26/07/1979" ,"Person7" : "04/09/1989" ,"Person8" : "09/06/1992","Person9" : "11/03/1994","Person10" : "10/01/1969" }


def checkbirth():
    x = input("Please enter the name: ")
    print(birthdays[x])
    


if __name__ == "__main__":
    checkbirth()
    
