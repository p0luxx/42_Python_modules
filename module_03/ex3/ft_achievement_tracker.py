#!/usr/bin/python3
import random


def get_achievements() -> tuple:
    achievements = (
        "Predator", "Alchemist", "Xenomaster", "Ignis mentis",
        "Vapula Oh Megas", "Western killer", "Mental Makoomba",
        "Xenoverse is here!", "Jason, are u there?", "Karaoke night",
        "Oh shit here we go again", "Speed Demon", "Iron Wall",
        "Silent Assassin", "Combo Master", "Last Stand",
        "Perfectionist", "Night Owl", "Early Bird", "Trailblazer",
        "Shadow Walker", "Relentless", "Untouchable", "Overkill",
        "Flawless Victory", "Comeback King", "Underdog", "Marathoner",
        "Sharpshooter", "Berserker", "Guardian", "Pathfinder", "Legend")
    return achievements


def gen_player_achievements() -> set:
    achievements = get_achievements()
    n = random.randint(1, 11)
    data = random.sample(achievements, n)
    return set(data)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    achievements = set(get_achievements())
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")
    print(f"All player disctinct achievements: "
          f"{set.union(alice, bob, charlie, dylan)}\n")
    print(f"Common achievements: "
          f"{set.intersection(alice, bob, charlie, dylan)}\n")
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    print(f"Alice is missing: {achievements.difference(alice)}")
    print(f"Bob is missing: {achievements.difference(bob)}")
    print(f"Charlie is missing: {achievements.difference(charlie)}")
    print(f"Dylan is missing: {achievements.difference(dylan)}")
