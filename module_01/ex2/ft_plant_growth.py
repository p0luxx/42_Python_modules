#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 2)}cm, {self.days} days old")

    def grow(self) -> None:
        self.height += 0.4

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    o_height = 0.6
    sunflower = Plant("Sunflower", 0.6, 12)
    i = 1
    print("=== Garden Plant Growth ===")
    print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.days} days old")
    while i <= 7:
        print(f"=== Day {i} ===")
        sunflower.age()
        sunflower.grow()
        sunflower.show()
        i += 1
    print(f"Growth this week: {round(sunflower.height - o_height)}cm")
