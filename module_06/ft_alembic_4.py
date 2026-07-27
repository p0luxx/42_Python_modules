#!/usr/bin/python3


import alchemy


if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    try:
        print("Now show that not all functions can be reached")
        print(alchemy.create_earth())
    except AttributeError as e:
        print(f"Testing the hidden create_earth: {e}")
