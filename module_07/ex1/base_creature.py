#!/usr/bin/python3

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, c_name: str, c_type: str) -> None:
        self.c_name = c_name
        self.c_type = c_type

    @abstractmethod
    def attack(self) -> str: ...

    def describe(self) -> str:
        return f"{self.c_name} is a {self.c_type} type Creature"
