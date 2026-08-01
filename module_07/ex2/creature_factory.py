#!/usr/bin/python3
from ex2.base_creature import Creature
from ex2.base_factory import CreatureFactory
from ex2.creatures import (
    Aquabub,
    Bloomelle,
    Flameling,
    Morphagon,
    Pyrodon,
    Shiftling,
    Sproutling,
    Torragon,
)


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        return Aquabub()

    def create_evolved(self) -> Torragon:
        return Torragon()


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
