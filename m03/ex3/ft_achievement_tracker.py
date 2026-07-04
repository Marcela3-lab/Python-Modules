import random

def gen_player_achievements():
    achievements = {"Crafting Genius", "Strategist", "World Savior", "Speed Runner", "Survivor", "Master Explorer",
    "Treasure Hunter", "Unstoppable", "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind", "Boss Slayer"}
    Alice = set(random.sample(list(achievements), 6))
    Bob = set(random.sample(list(achievements), 7))
    Charlie = set(random.sample(list(achievements), 9))
    Dylan = set(random.sample(list(achievements), 5))

    print(f"Player Alice: {Alice}")
    print(f"Player Bob: {Bob}")
    print(f"Player Charlie: {Charlie}")
    print(f"Player Dylan: {Dylan}")
    print(f"All distinct achievements: {achievements}")
    print()
    
    common = Alice.intersection(Bob, Charlie, Dylan)
    print(f"Common achievements: {common}")

    print()

    alice_unique = Alice.difference(Bob, Charlie, Dylan)
    bob_unique = Bob.difference(Alice, Charlie, Dylan)
    charlie_unique = Charlie.difference(Alice, Bob, Dylan)
    dylan_unique = Dylan.difference
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")
    print(f"Charlie unique: {charlie_unique}")
    print(f"Dylan unique: {dylan_unique}")

    print()

    missing_alice = achievements - Alice
    missing_bob = achievements - Bob
    missing_charlie = achievements - Charlie
    missing_dylan = achievements - Dylan
    print(f"Alice is missing: {missing_alice}")
    print(f"Bob is missing: {missing_bob}")
    print(f"Charlie is missing: {missing_charlie}")
    print(f"Dylan is missing: {missing_dylan}")

if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()
    gen_player_achievements()