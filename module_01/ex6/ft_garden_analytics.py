#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = ""
        self._height = 0.0
        self._age = 0
        self._stats = Plant.Stats(name)
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)
    @classmethod
    def set_default_params(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)
    @staticmethod
    def is_greater_a_year(age) -> bool:
        if age <= 365:
            return False
        else:
            return True
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
        self._stats.show_count += 1
        return f"{self._name}: {round(self._height, 2)}cm, {self._age} days old"
    class Stats:
        def __init__(self, name:str) -> None:
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0
            self.name = name
        def show_stats(self) -> None:
            print(f"[statistics for {self.name}]")
            print(f"Stats: {self.grow_count} grow, {self.age_count} age, {self.show_count} show")

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
        self._stats = Tree.ShadeCount(name)
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
        self._stats.shade_count += 1
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height}cm long and {self._diameter}cm wide.")
    def print_stats(self) -> None:
        stats = super().get_stats()
        print("=== Tree")
        print(f"{stats}")
        print(f"Trunk diameter: {self._diameter}cm")
    class ShadeCount(Plant.Stats):
        def __init__(self, name:str) -> None:
            super().__init__(name)
            self.shade_count = 0
        def show_stats(self) -> None:
            print(f"[statistics for {self.name}]")
            print(f"Stats: {self.grow_count} grow, {self.age_count} age, {self.show_count} show, {self.shade_count} shade")

class Vegetable(Plant):
    def __init__(self, season:str, n_value:int, name:str, height:float, age:int):
        super().__init__(name, height, age)
        self._season = ""
        self._n_value = 0
        self.set_season(season)
        self.set_n_value(n_value)
    def get_season(self) -> str:
        return self._season
    def get_n_value(self) -> int:
        return self._n_value
    def set_season(self, value:str) -> None:
        self._season = value
    def set_n_value(self, value:int) -> None:
        if value < 0:
            print("Error: Nutritional value can't be a negative number")
        else:
            self._n_value = value
    def grow(self, days:int) -> None:
        print(f"[make {self._name} grow and age for {days} days]")
        for day in range(days):
            self._height += 0.1
            self._age += 1
            self._n_value += 1
        stats = super().get_stats()
        self._stats.grow_count += 1
        print(f"{stats}")
        print(f" Harvest season: {self._season}")
        print(f" Nutritional value: {self._n_value}")
    def print_stats(self) -> None:
        print("=== Vegetable")
        stats = super().get_stats()
        print(f"{stats}")
        print(f" Harvest season: {self._season}")
        print(f" Nutritional value: {self._n_value}")
class Seed(Flower):
    def __init__(self, quantity:int, color:str, name:str, height:float, age:int) -> None:
        super().__init__(color, name, height, age)
        self._quantity = 0
        self.set_quantity(quantity)
    def get_quantity(self) -> str:
        return self._quantity
    def set_quantity(self, value:int) -> None:
        if value < 0:
            print("Error: Quanity seeds can't be a negative number")
        else:
            self._quantity = value
    def bloom(self) -> None:
        super().bloom()
        self._quantity += 1
    def print_stats(self) -> None:
        print("=== Seed")
        super().print_stats()
        print(f"Seeds: {self._quantity}")
if __name__ == "__main__":

    print("=== Garden Plant Types ===")
    rose = Flower("red", "Rose", 15.0, 10)
    oak = Tree(5.0, "Oak", 200.0, 365)
    tomato = Vegetable("April", 0, "Tomato", 5.0, 10)
    seed = Seed(0, "yellow", "Sunflower", 80.0, 45)
    anonimous = Plant.set_default_params()
    rose.print_stats()
    rose.bloom()
    oak.print_stats()
    oak.produce_shade()
    tomato.print_stats()
    tomato.grow(20)
    seed.print_stats()
    seed.bloom()
    anonimous.print_stats()

