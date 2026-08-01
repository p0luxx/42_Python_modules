#!/usr/bin/python3

from ex2 import (
    AggressiveStrategy,
    AquaFactory,
    DefensiveStrategy,
    FlameFactory,
    HealingCreatureFactory,
    InvalidStrategyError,
    NormalStrategy,
    TransformCreatureFactory,
)


def battle(opponents: list) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            c1, s1 = opponents[i]
            c2, s2 = opponents[j]
            print("* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")
            try:
                s1.act(c1)
                s2.act(c2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main():
    flame_fac = FlameFactory()
    aqua_fac = AquaFactory()
    healing_fac = HealingCreatureFactory()
    transform_fac = TransformCreatureFactory()
    normal_strat = NormalStrategy()
    aggressive_strat = AggressiveStrategy()
    defensive_strat = DefensiveStrategy()
    battle(
        [
            (flame_fac.create_base(), normal_strat),
            (healing_fac.create_base(), defensive_strat),
        ]
    )
    print()
    battle(
        [
            (flame_fac.create_base(), aggressive_strat),
            (healing_fac.create_base(), defensive_strat),
        ]
    )
    print()
    battle(
        [
            (aqua_fac.create_base(), normal_strat),
            (healing_fac.create_base(), defensive_strat),
            (transform_fac.create_base(), aggressive_strat),
        ]
    )


if __name__ == "__main__":
    main()
