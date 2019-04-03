#  File: Dice.py
#  Description: Simulate a dice roll for 2 six-sided die and print a histogram of the outcome
#  Student's Name: Samuel Randall
#  Student's UT EID: spr699
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 09/12/17
#  Date Last Modified: 09/14/17

import random

def main():
    random.seed(1314)

    # amount of times dice are to be thrown via input from the user
    rollCount = int(input("How many times do you want to roll the dice? "))

    # The position in the list represents the result of the roll and the
    # value is the amount of times that number was rolled
    rollResults = [0,0,0,0,0,0,0,0,0,0,0]

    # adding two 0-5 random ints together simulates 2 six sided die being rolled
    for i in range(1,rollCount):
        rollValue = random.randint(0,5) + random.randint(0,5)
        rollResults[rollValue] += 1       
    print("Results: " + str(rollResults))

    histogram(rollCount, rollResults)
   
# printing the correct amount of spaces and *'s
def histogram(rollCount, rollResults):
    if (rollCount > 100):
        for i in range(0,11):
            rollResults[i] = round(rollResults[i] * (100/rollCount))
            
    # we need to find the greatest value in the list to know what * to place at the top
    topValue = max(rollResults)

    while(topValue > 0):  #printing of the stars and spaces
        print("|  ", end="")
        for number in range(0,11):
            if rollResults[number] == topValue:
                print("*  ", end="")
                rollResults[number] -= 1
            else:
                print("   ", end="")
        print()            
        topValue -= 1

    print("+--+--+--+--+--+--+--+--+--+--+--+-")
    print("   2  3  4  5  6  7  8  9 10 11 12")

main()


