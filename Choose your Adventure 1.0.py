# Programmer: Lauryn Meyer
# Date: 3-15-2024
# Program: Choose your own Adventure

# Encounter 1
import random

def print_instructions():
    print("Your mission is to safely pet as many cats as possible!")
    print("Choose the wrong cat and you may end up with a scratch.\n")

def pet_cat(cat_type, decrease_health):
    global health, pets
    print("\nYou see a", cat_type, "cat! You are dying to pet it.")
    print("The cat seems a little skittish. Do you pet the", cat_type, "cat?")
    choice = input("Type 'Y' for Yes or 'N' for No: ").lower()
    print(" ")
    if choice == "y":
        health -= decrease_health
        print("You reach out to pet the", cat_type, "cat and it swats your hand away, leaving you with a scratch.")
        print("The cat has decreased your health by", decrease_health, "resulting in your health level decreasing to", health)
        print("You should really get to know the cat better first. The cat then runs off ahead of you.")
        pets += 1
    else:
        print("Great choice, you have decided to not pet the", cat_type, "cat.")
        print("You should really get to know it better first. Your health remains at", health)
        print("The cat runs off ahead exposing a path you decide to follow.\n")

def encounter_cat():
    if health > 0:
        print("\nYou have just walked into the sacred forest of cats and have a health level of", health)
        cat_types = ["black", "white", "calico", "tabby"]
        chosen_cat = random.choice(cat_types)
        if chosen_cat == "black":
            pet_cat("black", dcrsHlthMnr)
        elif chosen_cat == "white":
            pet_cat("white", dcrsHlthMjr)
        elif chosen_cat == "calico":
            pet_cat("calico", dcrsHlthMjr)
        elif chosen_cat == "tabby":
            pet_cat("tabby", dcrsHlthMnr)
    else:
        print("Sorry, you did not get to pet any cats.")

if __name__ == "__main__":
    print_instructions()

    health = 5
    dcrsHlthMjr = 5
    dcrsHlthMnr = 2
    pets = 0

    encounter_cat()

# Encounter 2