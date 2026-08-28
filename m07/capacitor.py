import ex1


def test_healing_factory(factory) -> None:
    base = factory.creat_base()
    evolved = factory.creat_evolved()

    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform_factory(factory) -> None:
    base = factory.creat_base()
    evolved = factory.creat_evolved()

    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


print("Testing Creature with healing capability")

heal = ex1.HealingCreatureFactory()

test_healing_factory(heal)

print()

print("Testing Creature with transform capability")

transform = ex1.TransformCreatureFactory()

test_transform_factory(transform)
