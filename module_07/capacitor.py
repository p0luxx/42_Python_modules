#!/usr/bin/python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_healing_creatures(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, HealCapability):
        print(base.heal())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, HealCapability):
        print(evolved.heal())


def test_transform_creatures(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.transform())
        print(base.attack())
        print(base.revert())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, TransformCapability):
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


if __name__ == "__main__":
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    test_healing_creatures(healing_factory)
    print()
    test_transform_creatures(transform_factory)
