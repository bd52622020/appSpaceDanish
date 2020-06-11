#!/usr/bin/env python

import random

def myteamcalc(name, wins, loss = 0, draws = 0):
    points = 0
    points += wins * 3
    points += draws
    print("Your teams points are" ,points)
    Taunts = {"Good":"Try to improve", "Middle":"Could do better", "Bad":"train harder!"}
    gdcomments = {1:"nice job", 2:"well played", 3:"they did will!"}
    bdcomments = {1:"Aweful job", 2:"terrible!", 3:"maybe pick a different team to support"}
    if points < 20:
        print(random.choice(list(Taunts.values())) + random.choice(list(bdcomments.values())))
    else:
        print(random.choice(list(Taunts.values())) + ", " + random.choice(list(gdcomments.values())))


if __name__ == "__main__":
    one = input("Please enter the name of your team: ")
    two = input("Please enter the wins: ")
    three = input("Please enter the losses: ")
    four = input("Please enter the draws: ")
    myteamcalc(one, two, three, four)
