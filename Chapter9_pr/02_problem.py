#  problem: Write a program to implement a game where you have to guess a number between 1 to 100.
#  You have to keep track of your high score in a file. If you break the high score, you should update it.

import random

def game():
    print("You are playing a game")
    
    score =random.randint(1, 100)    
    # Fetch the highscore
    with open ("highscore.txt") as f:
        highscore = f.read()
        if(highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"Your score is {score} and highscore is {highscore}")
    if(score>highscore):
        # write this highscore to file
        with open("highscore.txt","w") as f:
            f.write(str(score))
            print("You have just broken the high score")

    return score

game()