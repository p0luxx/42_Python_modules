#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = ""
        self._height = 0.0
        self._age = 0
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_name(self, value: str) -> None:
        self._name = value

    def set_height(self, value: float) -> None:
        if value < 0:
            print("Error: height can't be a negative number")
        else:
            self._height = value

    def set_age(self, value: int) -> None:
        if value < 0:
            print("Error: age can't be a negative number")
        else:
            self._age = value

    def get_stats(self) -> str:
        return f"{self._name}: {self._height}cm, {self._age} days old"


class Flower(Plant):
    def __init__(self, color: str, name: str, height: float, age: int) -> None:
        super().__init__(name, height, age)
        self._color = ""
        self.set_color(color)

    def get_color(self) -> str:
        return self._color

    def set_color(self, value: str) -> None:
        self._color = value
    def	bloom(self)  -> None:
        stats = super().get_stats()
        print("[asking the rose to bloom]")
        print(f"{stats}")
        print(f" Color: {self._color}")
        print(" Rose is blooming beautifully!")
    def print_stats(self) -> None:
        stats = super().get_stats()
        print("=== Flower")
        print(f"{stats}")
        print(f" Color: {self._color}")
        print(" Rose has not bloomed yet")

class Tree(Plant):
    def __init__(self, diameter:float, name:str, height:float, age:int) -> None:
        super().__init__(name, height, age)
        self._diameter = 0.0
        self.set_diameter(diameter)
    def get_diameter(self) -> float:
        return self._diameter
    def set_diameter(self, value:float) -> None:
        if value < 0:
            print("Error: Trunk diameter value can't be a negative number")
        else:
            self._diameter = value
    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height}cm long and {self._diameter}cm wide.")
    def print_stats(self) -> None:
        stats = super().get_stats()
        print(f"{stats}")
        print(f"Trunk diameter: {self._diameter}")

if __name__ == "__main__":

    print("=== Garden Plant Types ===")
    rose = Flower("red", "Rose", 15.0, 10)
    oak = Tree(5.0, "Oak", 200.0, 365)
    rose.print_stats()
    rose.bloom()
    oak.print_stats()
    oak.produce_shade()