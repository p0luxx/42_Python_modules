#!/usr/bin/python3

import alchemy  # noqa: F401
import transmutation.recipes  # type: ignore[import-not-found]

if __name__ == "__main__":
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print(f"Testing lead to gold: {transmutation.recipes.lead_to_gold()}")
