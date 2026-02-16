stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def display_inventory(inventory):
    print("== Inventory ==")
    print("")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(k + ":", v )
    print("Total number of items: " + str(item_total))
    return 0

display_inventory(stuff)

def addToInventory(inventory, items):
    for item in items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory.setdefault(item, 0)
            inventory[item] += 1
    return inventory

addToInventory(stuff, ['torch', 'rope', 'human soul'])
display_inventory(stuff)

input()