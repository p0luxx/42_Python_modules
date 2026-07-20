import sys


def check_argument(arg: str) -> bool:
    is_valid = False
    if len(arg) == 0 or arg[0] == ":":
        return False
    for c in arg:
        if c == ":":
            is_valid = True
    return is_valid


def get_value(arg: str) -> int:
    to_convert = ""
    for i in range(0, len(arg)):
        if arg[i] == ":":
            for c in arg[i + 1:]:
                to_convert += c
            break
    if to_convert == "":
        raise ValueError("No quantity assigned")
    else:
        return int(to_convert)


def get_key(arg: str) -> str:
    key = ""
    for c in arg:
        if c == ":":
            break
        key += c
    return key


def make_inventory(args: list) -> dict:
    inventory = {}
    for i in range(1, len(sys.argv)):
        try:
            if check_argument(sys.argv[i]):
                key = get_key(sys.argv[i])
                try:
                    value = get_value(sys.argv[i])
                except ValueError as e:
                    print(f"Quantity error for '{key}': {e}")
                    continue
                if key in inventory:
                    print(f"Redundant item '{key}' - discarding")
                else:
                    inventory.update({key: value})
            else:
                print(f"Error - invalid parameter '{sys.argv[i]}'")
        except IndexError as e:
            print(f"Anomalous error: {e}")
    return inventory


def get_max_val(inventory: dict) -> str:
    temp = ""
    value = None
    for key in inventory.keys():
        if value is None or value < inventory[key]:
            value = inventory[key]
            temp = key
    return temp


def get_min_val(inventory: dict) -> str:
    temp = ""
    value = None
    for key in inventory.keys():
        if value is None or value > inventory[key]:
            value = inventory[key]
            temp = key
    return temp


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = make_inventory(sys.argv)
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory)}")
    print(f"Total quantity of the {len(inventory.keys())}"
          f" items: {sum(inventory.values())}")
    total = sum(inventory.values())
    for key in inventory.keys():
        value = inventory[key]
        percentage = (value / total * 100)
        print(f"Item {key} represents {round(percentage, 1)}%")
    try:
        item_max = get_max_val(inventory)
        item_min = get_min_val(inventory)
        print(f"Item most abundant: {item_max}"
              f" with quantity {inventory[item_max]}")
        print(f"Item least abundant: {item_min}"
              f" with quantity {inventory[item_min]}")
    except KeyError:
        pass
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
