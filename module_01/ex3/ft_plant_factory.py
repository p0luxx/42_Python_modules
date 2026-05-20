#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def stats(self) -> str:
        res = f"{self.name}: {self.height}cm, {self.age} days old"
        return res


if __name__ == "__main__":
    plant_set = [
        Plant("Sunflower", 0.9, 22),
        Plant("Tomato", 1.77, 21),
        Plant("Lettuce", 1.21, 2),
        Plant("Tobbaco", 2.19, 144),
        Plant("Palm Tree", 12.87, 4719),
    ]
    print("=== Plant factory Output ===")
    for plant in plant_set:
        print(f"Created: {plant.stats()}")
