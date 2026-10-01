# Say you’re creating a medieval fantasy video game. The data structure to model the player’s inventory is a dictionary whose keys are strings describing the item in the inventory and whose values are integers detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has one rope, six torches, 42 gold coins, and so on.

# Write a function named display_inventory() that would take any possible “inventory” and display it like the following:

# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62


stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12, "partyhat": 2, "rune scimitar": 1}

def display_inventory(inventory):
    print("Inventory:")
    inventory_item_total = 0
    for inventory_item_key, inventory_item_value in inventory.items():
        print(f"{inventory_item_value} {inventory_item_key}")
        inventory_item_total = inventory_item_total + inventory_item_value
        # FILL THIS PART IN
    print("Total number of items: " + str(inventory_item_total))
display_inventory(stuff)
