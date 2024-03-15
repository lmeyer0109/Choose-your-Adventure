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
    choice = input("Type 'Y' for Yes or 'N' for No: ").lower()
    if choice == "y":
        health -= decrease_health
        print(f"You reach out to pet the {cat_type} cat and it swats your hand away, leaving you with a scratch.")
        print(f"The cat has decreased your health by {decrease_health}, resulting in your health level decreasing to {health}.")
        print("You should really get to know the cat better first. The cat then runs off ahead of you.")
        pets += 1
    else:
        print(f"Great choice, you have decided to not pet the {cat_type} cat.")
        print("You should really get to know it better first. Your health remains at", health)
        print("The cat runs off ahead exposing a path you decide to follow.\n")

def encounter_cat():
    global health
    if health > 0:
        print(f"\nYou have just walked into the sacred forest of cats and have a health level of {health}")
        cat_types = ["black", "white", "calico", "tabby"]
        chosen_cat = random.choice(cat_types)
        decrease_health = 5 if chosen_cat in ["white", "calico"] else 2
        pet_cat(chosen_cat, decrease_health)
    else:
        print("Sorry, you did not get to pet any cats.")

if __name__ == "__main__":
    print_instructions()
    health, pets = 5, 0
    encounter_cat()


# Encounter 2