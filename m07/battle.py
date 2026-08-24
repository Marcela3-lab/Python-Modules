from ex0 import FlameFactory, AquaFactory


def test_factory(factory):
    base = factory.creat_base()
    evolved = factory.creat_evolved()

    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack())


def battle(factory1, factory2):
    creature1 = factory1.creat_base()
    creature2 = factory2.creat_base()

    print(f"{creature1.describe()} vs. {creature2.describe()}")
    print("fight!")
    print(creature1.attack())
    print(creature2.attack())


flame_factory = FlameFactory()
aqua_factory = AquaFactory()

test_factory(flame_factory)
print()
test_factory(aqua_factory)
print()
battle(flame_factory, aqua_factory)