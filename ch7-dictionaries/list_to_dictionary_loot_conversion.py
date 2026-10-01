# Imagine that the same fantasy video game represents a vanquished dragon’s loot as a list of strings, like this:

# dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Write a function named add_to_inventory(inventory, added_items). The inventory parameter is a dictionary representing the player’s inventory (as in the previous project) and the added_items parameter is a list, like dragon_loot. The add_to_inventory() function should return a dictionary that represents the player’s updated inventory. Note that the added_items list can contain multiples of the same item. Your code could look something like this:

def display_inventory(inventory):
    print("Inventory:")
    inventory_item_total = 0
    for inventory_item_key, inventory_item_value in inventory.items():
        print(f"{inventory_item_value} {inventory_item_key}")
        inventory_item_total = inventory_item_total + inventory_item_value
    print("Total number of items: " + str(inventory_item_total))

def add_to_inventory(inventory, added_items):
    count_inventory_item = {}
    for item in added_items:
        count_inventory_item.setdefault(item, 0)
        count_inventory_item[item] = count_inventory_item[item] + 1
    return count_inventory_item

inventory = {'gold coin': 42, 'rope': 1}
dragon_raid_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'name change token', 'the real true piece of the holy cross']

inventory = add_to_inventory(inventory, dragon_raid_loot)
display_inventory(inventory)

#none of values in add to inv function are getting caught meaning that these values anrent being operated on at all
# added items and dragon raid loot incongruence? im a little confused
