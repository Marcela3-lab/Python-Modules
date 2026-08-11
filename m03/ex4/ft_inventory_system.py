import sys


def parse_inventory(args: list) -> dict:
    inventory: dict[str, int] = {}

    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        name, quat = arg.split(":")

        if name in inventory.keys():
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            qty = int(quat)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue

        inventory.update({name: qty})

    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    args = sys.argv[1:]
    inventory = parse_inventory(args)
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the '{len(inventory)}"
          f"'items: {sum(inventory.values())}")
    total = sum(inventory.values())

    for item in inventory.keys():
        qty = inventory[item]
        percentagem = round(qty/total*100, 1)
        print(f"Item '{item}' represents {percentagem}")

    items = list(inventory.keys())
    most_item = items[0]
    least_item = items[0]

    for item in inventory.keys():
        if inventory[item] > inventory[most_item]:
            most_item = item
        if inventory[item] < inventory[least_item]:
            least_item = item

    print(f"Item most abundant: {most_item} "
          f"with quantity {inventory[most_item]}")
    print(f"Item least abundant: {least_item} with "
          f"quantity {inventory[least_item]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
