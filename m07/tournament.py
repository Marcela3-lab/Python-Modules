import ex0
import ex1
import ex2

flame_fac = ex0.FlameFactory
aqua_fac = ex0.AquaFactory
heal_fac = ex1.HealingCreatureFactory
transf_fac = ex1.TransformCreatureFactory

normal = ex2.NormalStrategy
aggressive = ex2.AggressiveStrategy
defensive = ex2.DefensiveStrategy


def battle(opponents):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()
    print("* Battle *")

    for i in range(len(opponents)):
        for j in range(i+1, len(opponents)):
            factory1, strat1 = opponents[i]
            factory2, strat2 = opponents[j]

            creature1 = factory1.creat_base()
            creature2 = factory2.creat_base()

            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")

            print(creature1.attack())
            print(creature2.attack())
            print(creature2.heal())

            action1 = strat1.act(creature1)
            for action in action1:
                print(action)


print("Tournament 0 (basic)")
opponents = [(flame_fac(), normal()), (heal_fac(), defensive())]
battle(opponents)
print()
print("Tournament 1 (error)")
opponents = [(flame_fac(), aggressive()), (heal_fac(), defensive())]
battle(opponents)