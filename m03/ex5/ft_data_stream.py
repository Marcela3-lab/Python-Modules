import random
from typing import Generator


def gen_event() -> Generator:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "move", "grab", "release", "climb", "swim", "use"]

    while True:
        yield (
            random.choice(players),
            random.choice(actions)
        )


def consume_event(events) -> Generator:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        yield events.pop(index)


print("=== Game Data Stream Processor ===")

events = gen_event()

for i in range(1000):
    player, action = next(events)
    print(f"Event {i}: Player {player} did action {action}")

event_list = []

for i in range(10):
    event_list.append(next(events))

print(f"Built list of 10 events: {event_list}")

for event in consume_event(event_list):
    print(f"Got event from list: {event}")
    print(f"Remains in list: {event_list}")