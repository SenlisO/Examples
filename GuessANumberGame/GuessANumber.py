"""
Guess a Number Program
This technical demo generates a random number and lets the player attempt to guess the number
"""

import random

# step 1: display an intro
print ("Guess A Number Game")
print ("A technical demo by Richard Romick")

# step 2: initialize variables and generate random number
game_over = False
answer = random.randint(0, 100) # this will generate a number between 0 and 100 inclusive
print ("answer is %s" % answer)

# step 3: begin game loop
while not game_over:
    # step 4: allow the user to guess a number
    print ("--------------------------------------")
    raw_guess = raw_input("Guess a number between 0 and 100 inclusive ('q' to quit):")

    # step 5: end program if the user wants to quit
    if raw_guess == "q":
        game_over = True
    else: # step 6: evaluate guess and print result
        guess = int(raw_guess)
        if guess < answer:
            print ("Your guess was too low")
        elif guess > answer:
            print ("Your guess was too high")
        else:
            print ("You Win!")
            game_over = True

