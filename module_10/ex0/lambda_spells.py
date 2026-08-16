artifact_sorter = lambda arti: sorted(arti, key=lambda x: x["power"], reverse=True)  # noqa
power_filter = lambda mages, min_power: list(filter(lambda m: m["power"] >= min_power, mages))  # noqa
spell_transformer = lambda spells: list(map(lambda s: f"* {s} *", spells))  # noqa
mage_stats = lambda mages: {
    "max_power": max(map(lambda m: m["power"], mages)),
    "min_power": min(map(lambda m: m["power"], mages)),
    "avg_power": round(sum(map(lambda m: m["power"], mages)) / len(mages), 2),
} # noqa


if __name__ == "__main__":
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "Divination"},
        {"name": "Fire Staff", "power": 92, "type": "Evocation"},
    ]
    print("Testing artifact sorter...")
    n_art = artifact_sorter(artifacts)
    print(
          f"{n_art[0]['name']} ({n_art[0]['power']} power)"
          " comes before "
          f"{n_art[1]['name']} ({n_art[1]['power']} power)"
        )
    print("Testing power filter...\nPower filter -> 90")
    n_power = power_filter(artifacts, 90)
    print(f"{n_power[0]['name']} with power level {n_power[0]['power']}")
    print("Testing spells transformer...")
    spells = ["fireball", "heal", "shield"]
    res = spell_transformer(spells)
    print(res)
    mages = [
        {"name": "Gandalf", "power": 85},
        {"name": "Merlin", "power": 98},
        {"name": "Mimi", "power": 42},
    ]
    print("Testing mages stats...")
    res2 = mage_stats(mages)
    print(res2)
