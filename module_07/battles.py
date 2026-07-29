from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    basic_c = factory.create_base()
    evolved_c = factory.create_evolved()
    print(basic_c.describe())
    print(basic_c.attack())
    print(evolved_c.describe())
    print(evolved_c.attack())


def test_battle(f1: CreatureFactory, f2: CreatureFactory) -> None:
    print("Testing battle")
    basic1 = f1.create_base()
    basic2 = f2.create_base()
    print(basic1.describe())
    print(" vs.")
    print(basic2.describe())
    print(" fight!")
    print(basic1.attack())
    print(basic2.attack())


if __name__ == "__main__":
    fire_factory = FlameFactory()
    aqua_factory = AquaFactory()
    test_factory(fire_factory)
    print()
    test_factory(aqua_factory)
    print()
    test_battle(fire_factory, aqua_factory)
