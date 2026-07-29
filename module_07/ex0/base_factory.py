#!/usr/bin/python3

from abc import ABC, abstractmethod
from ex0.base_creature import Creature


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...
