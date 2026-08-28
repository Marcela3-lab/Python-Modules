import ex0


def test_factory(factory) -> None:
    base = factory.creat_base()
    evolved = factory.creat_evolved()

    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack())


def battle(factory1, factory2) -> None:
    creature1 = factory1.creat_base()
    creature2 = factory2.creat_base()

    print(f"{creature1.describe()} vs. {creature2.describe()}")
    print("fight!")
    print(creature1.attack())
    print(creature2.attack())


flame_factory = ex0.FlameFactory()
aqua_factory = ex0.AquaFactory()

print("Testing factory")
test_factory(flame_factory)
print()
print("Testing factory")
test_factory(aqua_factory)
print()
print("Testing battle")
battle(flame_factory, aqua_factory)
