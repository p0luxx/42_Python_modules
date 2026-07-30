#!/usr/bin/python3

import sys
from alchemy.elements import create_air
from alchemy import potions
from alchemy.potions import healing_potion as heal
from alchemy.transmutation import recipes
from alchemy import transmutation
sys.modules["transmutation"] = transmutation
sys.modules["transmutation.recipes"] = recipes
__all__ = ["create_air", "potions", "heal", "recipes"]


def create_earth() -> None:
    raise AttributeError("The 'create_earth' function "
                         "is not exposed in this module.")
