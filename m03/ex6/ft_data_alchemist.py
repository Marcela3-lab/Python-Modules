import random

def data_alchemist() -> None:
    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam"
    ]

    capitalized = [player.capitalize() for player in players]

    only_capitalized = [
        player
        for player in players
        if player[0].isupper()
    ]

    scores = {
        player: random.randint(0, 1000)
        for player in capitalized
    }

    average = round(sum(scores.values()) / len(scores), 2)

    high_scores = {
        player: score
        for player, score in scores.items()
        if score > average
    }

    print("=== Game Data Alchemist ===")
    print("Initial list of players:", players)
    print("New list with all names capitalized:", capitalized)
    print("New list of capitalized names only:", only_capitalized)
    print()
    print("Score dict:", scores)
    print("Score average is", average)
    print("High scores:", high_scores)


if __name__ == "__main__":
    data_alchemist()