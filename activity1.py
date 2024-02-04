import random

# Activity 1: Customizable Dice Simulator
def roll_dice(num_dice, num_sides):
    total = 0
    for _ in range(num_dice):
        roll = random.randrange(1, num_sides + 1)
        total += roll
    return total

num_dice = 2
num_sides = 6

result = roll_dice(num_dice, num_sides)
print(f"Rolling {num_dice} dice with {num_sides} sides each. Total:{result}")