#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = "no_name"
        self._height = 0.0
        self._age = 0
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_name(self) -> str:
        return self._name

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self._name}: Error: height can't be negative")
        else:
            self._height = value

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self._name}: Error: age can't be negative")
        else:
            self._age = value

    def set_name(self, name: str) -> None:
        self._name = name

    def stats(self) -> str:
        return f"{self._name}: {self._height}cm, {self._age} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print(f"Plant created: {rose.stats()}")
    rose.set_height(25.0)
    print("Height updated: 25cm")
    rose.set_age(30)
    print("Age updated: 30 days")
    rose.set_height(-4)
    print("Height updated rejected")
    rose.set_age(-6)
    print("Age update rejected")
    print(f"Current state: {rose.stats()}")
