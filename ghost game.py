import random
from random import randint
score = 0
print(" THE GHOST GAME")
game_on = True
while game_on:
    print("""there are three doors infront of you 
              one of it has ghost in it""")
    y = int(input("select the door number (1,2 or 3):"))
    x = randint(1, 3)
    if y == x:
        print("there is a ghost in it!")
        game_on = False
    else:
        print("the next level")

        score = score+1
print("GAME OVER, YOU ARE CAUGHT BY THE GHOST")
print("your score is ", score, '!')