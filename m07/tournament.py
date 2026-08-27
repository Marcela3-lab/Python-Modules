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

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strat1 = opponents[i]
            factory2, strat2 = opponents[j]

            creature1 = factory1.creat_base()
            creature2 = factory2.creat_base()
            print()
            print("* Battle *")
            print()
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")

            try:
                print(strat1.act(creature1))
                print(strat2.act(creature2))
            except ValueError as e:
                print(f"Error: {e}")


print("-" * 20)
print("Tournament 0 (basic)")
print("[ (Flameling+Normal), (Healing+Defensive) ]")
opponents = [(flame_fac(), normal()), (heal_fac(), defensive())]
battle(opponents)
print()
print("------------------------")
print("Tournament 1 (error)")
print("[ (Flameling+Normal), (Healing+Defensive) ]")
opponents = [(flame_fac(), aggressive()), (heal_fac(), defensive())]
battle(opponents)
print("------------------------")
print("Tournament 2 (multiple)")
print("[ (Aquabub+Normal), (Healing+Defensive),"
      "(Transform+Aggressive) ])")
opponents = [(aqua_fac(), normal()), (heal_fac(),
             defensive()), (transf_fac(), aggressive())]
battle(opponents)
