#!/usr/bin/python3

from abc import ABC, abstractmethod

from ex2 import (
    Creature,
    HealCapability,
    InvalidStrategyError,
    TransformCapability
)


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool: ...
    @abstractmethod
    def act(self, creature: Creature) -> None: ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.c_name}'"
                " for this normal strategy"
            )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.c_name}'"
                "for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, HealCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.c_name}'"
                "for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())
