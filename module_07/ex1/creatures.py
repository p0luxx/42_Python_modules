#!/usr/bin/python3

from ex1.base_creature import Creature
from ex1.capabilities import HealCapability, TransformCapability

class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return (f"{self.c_name} uses Ember!")


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return (f"{self.c_name} uses Flamethrower!")


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return (f"{self.c_name} uses Water Gun!")


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return (f"{self.c_name} uses Hydro Pump!")


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return (f"{self.c_name} uses Vine Whip!")

    def heal(self) -> str:
        return (f"{self.c_name} heals itself for a small amount")


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return (f"{self.c_name} uses Petal Dance!")

    def heal(self) -> str:
        return (f"{self.c_name} heals itself and others for a large amount")


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_evolved:
            return (f"{self.c_name} performs a boosted strike!")
        else:
            return (f"{self.c_name} attacks normally.")

    def transform(self) -> str:
        self.is_evolved = True
        return (f"{self.c_name} shifts into a sharper form!")

    def revert(self) -> str:
        self.is_evolved = False
        return (f"{self.c_name} returns to normal.")


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)


    def attack(self) -> str:
        if self.is_evolved:
            return (f"{self.c_name} unleashes a devastating morph strike!")
        else:
            return (f"{self.c_name} attacks normally.")

    def transform(self) -> str:
        self.is_evolved = True
        return (f"{self.c_name} morphs into a dragonic battle form!")

    def revert(self) -> str:
        self.is_evolved = False
        return (f"{self.c_name} stabilizes its form.")

