import time
import random
import math
# A HUGE COMMENT
# Introduction
print("Welcome to Jungle Quest!")
time.sleep(1)
print("You're a brave explorer trying to find a legendary treasure deep in the jungle...")
time.sleep(1)

# Variables
player_name = input("First, what's your name, explorer? ")
health = 100
inventory = []

print(f"\nWelcome, {player_name}! Your journey begins now. You have {health} health points.\n")

# First choice – Conditionals + Input
print("You reach a fork in the jungle path.")
choice1 = input("Do you want to go left into the dark cave or right toward the river? (left/right): ")

if choice1.lower() == "left":
    print("You enter the dark cave...")
    time.sleep(1)
    print("A bat swoops down and bites you!")
    health -= 20  # Math operator
    print("You lose 20 health points.")
    inventory.append("Bat Scratch")  # List usage
elif choice1.lower() == "right":
    print("You walk toward the river and find clean water.")
    time.sleep(1)
    print("You gain 10 health points.")
    health += 10
    inventory.append("Water Bottle")
else:
    print("You stand still too long. A monkey steals your map!")
    inventory.append("Missing Map")
    health -= 10

print(f"Current health: {health}")
print(f"Inventory: {inventory}\n")

# Random Event – Using random library
print("You find a treasure chest! Let's see what you get...")
treasures = ["Gold Coin", "Magic Potion", "Empty Chest"]
found = random.choice(treasures)
inventory.append(found)
print(f"You found: {found}\n")

# Loop – Asking multiple times
for i in range(3):
    guess = int(input(f"Guess a number between 1 and 5 (Attempt {i+1}): "))
    secret = random.randint(1, 5)
    if guess == secret:
        print("You guessed right! You gain a magic shield!")
        inventory.append("Magic Shield")
        break
    else:
        print("Wrong guess!")

# Function usage
def final_battle(health):
    print("\nYou reach the final gate where a giant snake blocks your path!")
    action = input("Do you want to fight or run? (fight/run): ")

    if action.lower() == "fight":
        power = math.floor(health * 0.2) + random.randint(5, 15)
        print(f"You attack with power level {power}!")
        if power > 20:
            print("You defeat the snake and find the treasure!")
        else:
            print("The snake defeats you. Game Over.")
    else:
        print("You run away safely... maybe next time you'll be braver!")

# Call the function
final_battle(health)

# Ending
print("\nYour final inventory:")
for item in inventory:
    print("-", item)

print("\nThanks for playing Jungle Quest!")
