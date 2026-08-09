import random
import typing


def gen_event() -> typing.Generator:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run",
               "eat",
               "sleep",
               "move",
               "grab",
               "release",
               "climb",
               "swim",
               "use"]

    while True:
        yield (
            random.choice(players),
            random.choice(actions)
        )


def consume_event(events: list) -> typing.Generator:
    while len(events) > 0:
         event=random.choice(events)
         events.remove(event)
         yield event

if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    events = gen_event()

    for i in range(1000):
        player, action = next(events)
        print(f"Event {i}: Player {player} did action {action}")

    lista = []
    item = gen_event()
    for i in range(10):
        lista.append(next(item)) 
    print(f"Built list of 10 events: {lista}")


    for event in consume_event(lista):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {lista}")