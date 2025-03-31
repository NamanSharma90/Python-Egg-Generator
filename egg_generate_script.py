import random
import json
import os

# egg attributes
colors = ["red", "green", "yellow", "blue", "purple", "black", "white"]
designs = ["spotted", "ingrained", "striped", "flying", "buried", "ancient", "cyberpunk"]
rarity_weights = {
    "normal": 60,  # 60% probability
    "super": 30,  # 30% probability
    "rare": 10  # 10% probability
}


EGG_DATA_FILE = "egg_data.json"
if os.path.exists(EGG_DATA_FILE):
    with open(EGG_DATA_FILE, "r") as file:
        egg_rarity_map = json.load(file)
else:
    egg_rarity_map = {}


def weighted_random_choice(weight_dict):

    choices, weights = zip(*weight_dict.items())
    return random.choices(choices, weights=weights, k=1)[0]


def generate_egg():

    color = random.choice(colors)
    design = random.choice(designs)
    egg_key = f"{design} {color}"


    if egg_key in egg_rarity_map:
        rarity = egg_rarity_map[egg_key]
    else:
        rarity = weighted_random_choice(rarity_weights)
        egg_rarity_map[egg_key] = rarity

    # Save updated egg data
    with open(EGG_DATA_FILE, "w") as file:
        json.dump(egg_rarity_map, file, indent=4)

    return f"You found the {design} {color} egg ({rarity})!"


def show_all_eggs():
    """Displays all eggs found so far in a neat list."""
    if not egg_rarity_map:
        print("You haven't found any eggs yet!")
        return

    print("\n🌟 Your Egg Collection 🌟")
    for i, (egg, rarity) in enumerate(egg_rarity_map.items(), start=1):
        print(f"{i}. {egg} ({rarity})")
    print("\nType 'exit' to go back to generating eggs.\n")



print("Press Enter to generate an egg, type 'valve' to see your collection, or type 'exit' to quit.")

while True:
    user_input = input().strip().lower()

    if user_input == "exit":
        print("Goodbye!")
        break
    elif user_input == "valve":
        while True:
            show_all_eggs()
            valve_input = input().strip().lower()
            if valve_input == "exit":
                print("Returning to egg generation...")
                break
    else:
        print(generate_egg())
