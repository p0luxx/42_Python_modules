#!/usr/bin/env python3


def ft_garden_intro(name: str, height: float, age: float):
    if name:
        info_name = name
        print(f"Plant: {info_name.capitalize()}")
    if height:
        info_height = height
        print(f"Height: {info_height}cm")
    if age:
        info_age = age
        print(f"Age: {info_age} days")


if __name__ == "__main__":
    ft_garden_intro("Calendula", 19, 0.7)
