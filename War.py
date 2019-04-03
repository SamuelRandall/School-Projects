#  File: War.py
#  Description: Simulate a game of war
#  Student's Name: Samuel Randall
#  Student's UT EID: spr699
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 10/4/17
#  Date Last Modified:10/6/17

import random

class Card:

    # begin by creating a list of values to represent each card
    values = {str(i): i for i in range(2, 11)}

    # setting the values for Jack Queen and King
    for num in ["J", "Q", "K"]:
        values[num] = 10

    # setting the value for Ace
    values["A"] = 11

    # we want these instance variables readily accessable
    def __init__(self, suit, rank):
        self.suit = str(suit)
        self.rank = str(rank)
        self.values = Card.values[self.rank]

    def __str__(self):
        return self.rank + self.suit

class Deck:

    # this populates a deck upon creation with sorted cards
    def __init__(self):
        self.cardList = [Card(newSuit, newRank) for newSuit in ["C", "D", "H", "S"]
            for newRank in list(range(2, 11)) + ["J", "Q", "K", "A"]]

    # this will print a list of the cards and their position
    def __str__(self):
        length = len(self.cardList)

        line = ""

        for num in range(length):
            if(num % 13):
                line += str(self.cardList[num]).rjust(4)
            else:
                line += "\n" + str(self.cardList[num]).rjust(4)
        return line + "\n"


    def shuffle(self):
        random.shuffle(self.cardList)

    # creating the action of dealing a card
    def dealOne(self, player):
        # retrieve the card
        card = self.cardList[0]
        # take the card out of the deck
        self.cardList.pop(0)
        # place the card to the player's deck
        player.hand.append(card)
        player.handTotal += 1

class Player:
    
    def __init__(self):
        self.hand = []
        self.handTotal = 0

    def __str__(self):
        # hold the string
        newHand = ""

        # hold count
        count = 1
        for num in range(len(self.hand)):

            space = "  "
            if len(str(self.hand[num])) == 3:
                space = " "

            newHand += space + str(self.hand[num])

            if count % 13 == 0 and count != 0:
                newHand += "\n"
            count += 1

        return newHand

    # checks to see if hand is empty and returns boolean
    def handNotEmpty(self):
        handEmpty = False 
        if(len(self.hand) == 0):
            handEmpty = True
        return handEmpty

    def playCard(self):
        playCard = self.hand.pop(0)
        self.handTotal -= 1
        return playCard

def playGame(deck, p1, p2):

    # must keep track of the rounds in order to iterate the loop
    rounds = 1
    
    while True:
        
        try:
            #create temporary decks for each round to test on and determine a winner
            roundCardsP1 = []
            roundCardsP2 = []

            p1Card = p1.playCard()
            roundCardsP1.append(p1Card)

            p2Card = p2.playCard()
            roundCardsP2.append(p2Card)

            # in case of a tie start war
            while p1Card.rank == p2Card.rank:
                
                for num in range(0,3):
                    p1DownCard = p1.playCard()
                    roundCardsP1.append(p1DownCard)
                    p2DownCard = p2.playCard()
                    roundCardsP2.append(p2DownCard)
                    
                p1Card = p1.playCard()
                p2Card = p2.playCard()

                roundCardsP1.append(p1Card)
                roundCardsP2.append(p2Card)

            # check to see the winner
            # player 1 wins
            if (p1Card.rank > p2Card.rank):
                for i in range(len(roundCardsP1)):
                    p1.hand.append(roundCardsP1[i])
                    p1.handTotal += 1
                    
                for i in range(len(roundCardsP2)):
                    p1.hand.append(roundCardsP2[i])
                    p1.handTotal += 1        

            # player 2 wins
            else:
                for i in range(len(roundCardsP1)):
                    p2.hand.append(roundCardsP1[i])
                    p2.handTotal += 1
                    
                for i in range(len(roundCardsP2)):
                    p2.hand.append(roundCardsP2[i])
                    p2.handTotal += 1
                    
            if (p1.handNotEmpty() and p2.handNotEmpty()):
                rounds += 1
            else:
                break
                    
        except IndexError:
            break

def main():

    cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
    print("Initial deck:")
    print(cardDeck)                 # print the deck so we can see that you built it correctly
    
    random.seed(15)                 # leave this in for grading purposes
    cardDeck.shuffle()              # shuffle the deck
    print("Shuffled deck:")
    print(cardDeck)                 # print the deck so we can see that your shuffle worked
    
    player1 = Player()              # create a player
    player2 = Player()              # create another player

    for i in range(26):             # deal 26 cards to each player, one at 
       cardDeck.dealOne(player1)    #   a time, alternating between players
       cardDeck.dealOne(player2)
    
    playGame(cardDeck,player1,player2)

    if player1.handNotEmpty():
        print("\n\nGame over.  Player 1 wins!")
    else:
        print("\n\nGame over.  Player 2 wins!")

    print ("\n\nFinal hands:")    
    print ("Player 1:   ")
    print (player1)                 # printing a player object should print that player's hand
    print ("\nPlayer 2:")
    print (player2)                 # one of these players will have all of the cards, the other none
    
main()



        
