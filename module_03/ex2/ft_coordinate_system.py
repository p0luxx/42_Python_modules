#!/usr/bin/python3
import math


def parser_input() -> tuple:
    while True:
        values: tuple[float, ...] = ()
        string = input("Enter new coordinates as floats in format 'x,y,z': ")
        buffer = ""
        counter = 0
        for i in string:
            if i == ",":
                counter += 1
        if counter == 2:
            try:
                for c in string:
                    if c == ",":
                        if buffer:
                            values += (float(buffer),)
                        buffer = ""
                    elif c != ",":
                        buffer += c
                values += (float(buffer),)
                return tuple(values)
            except ValueError as e:
                print(f"Error on parameter '{buffer}': {e}")
        else:
            print("Invalid syntax")


def get_player_pos() -> tuple:
    values = parser_input()
    return values


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    values = get_player_pos()
    x1 = values[0]
    y1 = values[1]
    z1 = values[2]
    print(f"Got a first tuple: {values}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    res = math.sqrt(((x1 - 0) ** 2) + ((y1 - 0) ** 2) + ((z1 - 0)**2))
    print(f"Distance to center: {round(res, 4)}\n")
    print("Get a second set of coordinates")
    values = get_player_pos()
    x2 = values[0]
    y2 = values[1]
    z2 = values[2]
    res = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2)**2))
    print(f"Distance between the 2 sets of coordinates: {round(res, 4)}")
