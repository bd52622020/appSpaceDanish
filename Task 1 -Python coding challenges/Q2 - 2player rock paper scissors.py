#!/usr/bin/env python


def game():
    x = input("Player 1, Please Choose rock, paper or scissors: ").lower()
    y = input("Player 2, Please Choose rock, paper or scissors: ").lower()
    
    if x == "rock" and y == "paper":
        print("Player 2 wins!")
    elif x == "rock" and y == "scissors":
        print("Player 1 wins!")
    elif x == "paper" and y == "rock":
        print("Player 1 wins!")
    elif x == "paper" and y == "scissors":
        print("Player 2 wins!")
    elif x == "scissors" and y == "rock":
        print("Player 2 wins!")
    elif x == "scissors" and y == "paper":
        print("Player 1 wins!")
    else:
        print("It was a draw! Try again!")
    print("Try playing again!")


if __name__ == "__main__":
    game()
