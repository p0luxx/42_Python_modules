#!/usr/bin/python3
import random
from typing import Generator


def gen_event() -> Generator[tuple, None, None]:
    players = ["bob", "alice", "dylan"]
    actions = ["run", "eat", "sleep", "move", "climb", "swim"]
    while True:
        user = random.choice(players)
        action = random.choice(actions)
        obj = (user, action)
        yield obj


def consume_event(events: list) -> Generator[tuple, list, None]:
    while len(events):
        index = random.randint(0, len(events) - 1)
        res = events[index]
        del events[index]
        yield res


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    test = gen_event()
    for i in range(0, 1000):
        info = next(test)
        print(f"Event {i}: Player {info[0]} did action {info[1]}")
    event_list: list[tuple] = []
    for i in range(0, 10):
        info = next(test)
        event_list += (info,)
    print(f"Built list of 10 events: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")
