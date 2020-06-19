import random

money = 100

# Write your game of chance functions here


def coin_flip(bet, call_side):
    global money
    coin = random.randint(1, 2)
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


#Call your game of chance functions here

coin_flip(16, "tails")

