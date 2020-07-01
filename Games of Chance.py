# Tien Phan
# Games of Chance

import random

# defined global variable
money = 100


# Write your game of chance functions here

# function that flips a coin and prints out the result
def newLine():
    return print("\n")

def coin_flip(bet, call_side):
    global money
    coin = random.randint(1, 2)
    print("Simulating coin flip...\n")
    print("---------------------------\n")

    if coin == 1 and call_side == "heads":
        money += bet
        return print("The coin is heads and you called the right side! You won "
                     + str(bet) + " and have currently " + str(money))
    elif coin == 2 and call_side == "tails":
        money += bet
        return print("The coin is tails and you called the right side! You won "
                     + str(bet) + " and have currently " + str(money))
    elif coin == 1 and call_side == "tails":
        money -= bet
        return print("The coin is heads and you called the wrong side! You lost "
                     + str(bet) + " and have currently " + str(money))
    else:
        money -= bet
        return print("The coin is tails and you called the wrong side! You lost "
                     + str(bet) + " and have currently " + str(money))


# function that simulates the game Cho-Han
def cho_han(bet, guess):
    global money
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    # dice1 = 2
    # dice2 = 2
    sumResult = dice1 + dice2
    print("Simulating Cho Han...\n")
    print("---------------------------\n")

#    if sumResult % 2 == 0 and guess == "even":
#        money += bet
#        return print("The result is " + str(sumResult) + " which is an even number and you won: "
#                     + str(bet) + " and have currently " + str(money))
    if (sumResult == 2 or sumResult == 4 or sumResult == 6 or sumResult == 8 or sumResult == 10 or sumResult == 12) and guess == "even":
        money += bet
        return print("The result is " + str(sumResult) + " which is an even number and you won: "
                     + str(bet) + " and have currently " + str(money))
    elif (sumResult == 3 or sumResult == 5 or sumResult == 7 or sumResult == 9 or sumResult == 11) and guess == "odd":
        money += bet
        return print("The result is " + str(sumResult) + " which is an odd number and you won: " + str(bet) + " and have currently " + str(money))
    elif (sumResult == 2 or sumResult == 4 or sumResult == 6 or sumResult == 8 or sumResult == 10 or sumResult == 12) and guess == "odd":
        money -= bet
        return print("The result is " + str(sumResult) + " which is an even number, your guess was an odd number so you lost: " + str(bet) + " and have currently " + str(money))
    else:
        money -= bet
        return print("The result is " + str(sumResult) + " which is an odd number, your guess was an even number so you lost: " + str(bet) + " and have currently " + str(money))


# function that simulates two players drawing from a deck of cards
def deck_of_cards(bet):
    global money
    player1 = random.randint(1, 52)
    player2 = random.randint(1, 52)
    print("Simulating Deck Of Cards...\n")
    print("---------------------------\n")

    if player1 > player2:
        money += bet
        return print("Your card is: " + str(player1) + "\nand the other player is: " + str(
            player2) + "\nYour card is higher so you won: "
                     + str(bet) + " and currently have:  " + str(money) + "\n")
    elif player2 > player1:
        money -= bet
        return print("Your card is: " + str(player1) + "\nand the other player is: " + str(
            player2) + "\nYour card is lower so you lost: "
                     + str(bet) + " and currently have:  " + str(money) + "\n")
    elif player1 == player2:
        print("Your card is: " + str(player1) + "\nand the other player is: " + str(
            player2) + "\nThe cards are the same and it's a tie so you don't win or lose money "
              + " and currently have:  " + str(money) + "\n")
        return 0


def roulette(bet, type, guess):
    global money
    num = random.randint(0, 36)
    print("Simulating roulette...\n")
    print("---------------------------\n")

    # types of bet
###########################################
    # color
    # single
    # low or high
    # odd or even
    # dozen
# to be implemented later
    # column
    # six line
    # square
    # street
    # split

    if type == "color":
        if num == 1 or 3 or 5 or 7 or 9 or 12 or 14 or 16 or 18 or 19 or 21 or 23 or 25 or 27 or 30 or 32 or 34 or 36:
            color = "red"
        elif num == 2 or 4 or 6 or 8 or 10 or 11 or 13 or 15 or 17 or 20 or 22 or 24 or 26 or 28 or 29 or 31 or 33 or 35:
            color = "black"

        if guess == color:
            money += bet + bet
            print("You bet: " + str(bet) + "\nand the color you chose was: " + guess + "\nit matches the roulette color and you won: " + str(bet) + "\nYou currently have: " + str(money))
        else:
            money -= bet
            print("You bet: " + str(bet) + "\nand the color you chose was: " + guess + "\nit does not matches the roulette color and you lost: " + str(bet) + "\nYou currently have: " + str(money))

    if type == "single":
        if guess == num:
            money += bet * 35
            print("You bet: " + str(bet) + "\nand the number you chose was: " + str(guess) + "\nit matches the roulette number and you won: " + str(bet) + "\nYou currently have: " + str(money))
        else:
            money -= bet
            print("You bet: " + str(bet) + "\nand the number you chose was: " + str(guess) + "\nit does not matche the roulette number and you lost: " + str(bet) + "\nYou currently have: " + str(money))

    if type == "low or high":
        if num == 0:
            money -= bet
            print("You guessed: " + guess + "\nthe number is: " + str(num) + "\nthis is not a low or high number so you lost: " + str(bet) + "\nyou currently have: " + str(money))
        elif guess == "low":
            if (num > 0 and num < 19):
                money += bet + bet
                print("You guessed: " + guess + "\nthe number is: " + str(num) + "\nthis is a low number so you won: " + str(bet) + "\nyou currently have: " + str(money))
            else:
                money -= bet
                print("You guessed: " + guess + "\nthe number is: " + str(num) + "\nthis is a high number so you lost: " + str(bet) + "\nyou currently have: " + str(money))
        elif guess == "high":
            if(num > 18 and num < 37):
                money += bet + bet
                print("You guessed: " + guess + "\nthe number is: " + str(num) + "\nthis is a high number so you won: " + str(bet) + "\nyou currently have: " + str(money))
            else:
                money -= bet
                print("You guessed: " + guess + "\nthe number is: " + str(num) + "\nthis is a low number so you lost: " + str(bet) + "\nyou currently have: " + str(money))
        else:
            print("Invalid input")

    if type == "odd or even":
        #if num == 0:
        #    money -= bet
        #    print("You guessed: " + guess + "\nthe number is: " + str(num) +
        #         "\nthis is not an odd or even number so you lost: " + str(bet)
        #         + "\nyou currently have: " + str(money))
        if guess == "odd" and (num == 1 or 3 or 5 or 7 or 9 or 11 or 13 or 15 or 17 or 19 or 21 or 23 or 25 or 27 or 29 or 31 or 33 or 35):
            money += bet + bet
            print("You guessed: " + str(guess) + "\nthe number is: " + str(num) + "\nthis is an odd number so you won: " + str(bet) + "\nyou currently have: " + str(money))
        elif guess == "even" and (num == 2 or 4 or 6 or 8 or 10 or 12 or 14 or 16 or 18 or 20 or 22 or 24 or 26 or 28 or 30 or 32 or 34 or 36):
            money += bet + bet
            print("You guessed: " + str(guess) + "\nthe number is: " + str(num) + "\nthis is an even number so you won: " + str(bet) + "\nyou currently have: " + str(money))
        elif guess == "odd" and (num != 1 or 3 or 5 or 7 or 9 or 11 or 13 or 15 or 17 or 19 or 21 or 23 or 25 or 27 or 29 or 31 or 33 or 35):
            money -= bet
            print("You guessed: " + str(guess) + "\nthe number is: " + str(num) + "\nthis is not an odd number so you lost: " + str(bet) + "\nyou currently have: " + str(money))
        elif guess == "even" and (num != 2 or 4 or 6 or 8 or 10 or 12 or 14 or 16 or 18 or 20 or 22 or 24 or 26 or 28 or 30 or 32 or 34 or 36):
            money -= bet
            print("You guessed: " + str(guess) + "\nthe number is: " + str(num) + "\nthis is not an even number so you lost: " + str(bet) + "\nyou currently have: " + str(money))
        else:
            "This is not a valid input"

    if type == "dozen":
        if guess == "first dozen" and (num > 0 and num < 13):
            money += bet * 2
            print("You guessed: " + guess + "\nthe number is: " + str(num) + "\nthis number is in the first dozen and you won: " + str(bet) + "\nyou currently have: " + str(money))
        elif guess == "second dozen" and (num > 12 and num < 25):
            money += bet * 2
            print("You guessed: " + guess + "\nthe number is: " + str(num) + "\nthis number is in the second dozen and you won: " + str(bet) + "\nyou currently have: " + str(money))
        elif guess == "third dozen" and (num > 24 and num < 37):
            money += bet * 2
            print("You guessed: " + guess + "\nthe number is: " + str(num) + "\nthis number is in the third dozen and you won: " + str(bet) + "\nyou currently have: " + str(money))
        else:
            money -= bet
            print("You guessed: " + guess + "\nthe number is: " + str(num) + "\nthis number is not in the guessed dozen so you lost: " + str(bet) + "\nyou currently have: " + str(money))

# Call your game of chance functions here

# tester function for coin flip function
coin_flip(16, "tails")
newLine()

# tester function for Cho-Han game
cho_han(10, "even")
newLine()
cho_han(10, "odd")
newLine()

#tester function for deck of cards game
deck_of_cards(10)

# tester function for roulette
roulette(10, "color", "red")
newLine()
roulette(10, "single", 5)
newLine()
roulette(10, "low or high", "low")
newLine()
roulette(10, "odd or even", "odd")
newLine()
roulette(10, "dozen", "first dozen")
