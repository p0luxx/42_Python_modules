#!/usr/bin/python3
from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    search_box = ingredients.lower()
    is_valid = any(item in search_box for item in allowed)
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
