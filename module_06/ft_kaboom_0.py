#!/usr/bin/python3

import alchemy.grimoire.light_spellbook

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    result = alchemy.grimoire.light_spellbook.light_spell_record(
        "Fantasy", "Earth, wind and fire"
    )
    print(f"Testing record light spell: {result}")
