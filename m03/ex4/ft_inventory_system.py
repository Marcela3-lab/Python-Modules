import sys

inventory = {}
order = []

for arg in sys.argv[1:]:
    if arg.count(":") != 1:
        print(f"Error - invalid parameter '{arg}'")
        continue

    item, quantity = arg.split(":")

    if item in inventory:
        print(f"Redundant item '{item}' - discarding")
        continue

    try:
        quantity = int(quantity)
    except ValueError as e:
        print(f"Quantity error for '{item}': {e}")
        continue

    inventory[item] = quantity
    order.append(item)

print("=== Inventory System Analysis ===")
print(f"Got inventory: {inventory}")
print(f"Item list: {list(inventory.keys())}")

total_quantity = sum(inventory.values())
print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

if total_quantity > 0:
    for item in inventory:
        percentage = round((inventory[item] / total_quantity) * 100, 1)
        print(f"Item {item} represents {percentage}%")

most_item = order[0]
least_item = order[0]

for item in order:
    if inventory[item] > inventory[most_item]:
        most_item = item
    if inventory[item] < inventory[least_item]:
        least_item = item

print(f"Item most abundant: {most_item} with quantity {inventory[most_item]}")
print(f"Item least abundant: {least_item} with quantity {inventory[least_item]}")

inventory.update({"magic_item": 1})

print(f"Updated inventory: {inventory}")