import random
from random import randint
import time
from time import sleep
score_ai = 0
score_ai =int(score_ai)
score_pl = 0
score_pl=int(score_pl)
n = 0
s_ai = ('rock' , 'paper' , 'scissor')
print("WELCOME TO ROCK PAPER AND SCISSOR GAME!")
print("HI I AM YOU OPPONENT  AI" )
y = input("READY TO PLAY WITH ME ?")
y = str.lower(y)
if y == 'yes':
    match_point =int(input("ENTER THE NUMBER OF POINTS TO WIN (ODD NUMBER):"))
    while score_ai or score_pl < match_point:
        n = n+1
        print("ROUND",n)
        ran = randint(0,2)
        aiw = s_ai[ran]
        print("READY!")
        sleep(0.5)
        print("ROCK!")
        sleep(0.5)
        print("PAPER!")
        sleep(0.5)
        print("SCISSOR!")
        sleep(0.5)
        plw = input("SHOOT!!:")
        plw = str.lower(plw)
        if aiw == plw:
            print("OOPS WE HAVE CHOOSEN THE SAME!HAHA!")
        elif aiw == 'rock' and plw == 'paper':
            print("MINE IS ", aiw, "AND YOUR'S IS ", plw)
            print("OH NO ! YOU HAVE WON THIS ROUND")
            score_pl = score_pl+1
            print("YOUR SCORE:", score_pl, '\t', "MY SCORE", score_ai)
        elif aiw == 'rock' and plw == 'scissor':
            print("MINE IS ", aiw, "AND YOUR'S IS ", plw)
            print("YEAH! I WON THIS ROUND")
            score_ai = score_ai+1
            print("YOUR SCORE:", score_pl, '\t', "MY SCORE", score_ai)
        elif aiw == 'paper' and plw == 'scissor':
            print("MINE IS ", aiw, "AND YOUR'S IS ", plw)
            print("OH NO ! YOU HAVE WON THIS ROUND")
            score_pl = score_pl+1
            print("YOUR SCORE:", score_pl, '\t', "MY SCORE", score_ai)
        elif aiw == 'paper' and plw == 'rock':
            print("MINE IS ", aiw, "AND YOUR'S IS ", plw)
            print("YEAH! I WON THIS ROUND")
            score_ai = score_ai+1
            print("YOUR SCORE:", score_pl, '\t', "MY SCORE", score_ai)
        elif aiw == 'scissor' and plw == 'rock':
            print("MINE IS ", aiw, "AND YOUR'S IS ", plw)
            print("OH NO ! YOU HAVE WON THIS ROUND")
            score_pl = score_pl+1
            print("YOUR SCORE:", score_pl, '\t', "MY SCORE", score_ai)
        elif aiw == 'scissor' and plw =='paper':
            print("MINE IS ", aiw, "AND YOUR'S IS ", plw)
            print("YEAH! I WON THIS ROUND")
            score_ai = score_ai+1
            print("YOUR SCORE:", score_pl, '\t', "MY SCORE", score_ai)
        else:
            print("I CANT'T UNDERSTAND THIS YOU FOOL!")

    if score_pl == 10:
        print("YOU HAVE ME !"+score_pl)
    else:
        print("I WON THIS GAME !!! BETTER LUCK NEXT TIME")


else:
    print("""JUST GET LOST! YOU ARE WASTING MY TIME 
                                                 by-AI""")
