from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} with {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int):
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int):
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int):
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int):
        results = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return sequence


if __name__ == "__main__":
    target = "Dragon"
    power = 10
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined result: {combined(target, power)}")
    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball(target, power)}")
    print(f"Amplified: {mega_fireball(target, power)}")
    print("\nTesting conditional caster...")
    def always_true(t, p): return True
    def always_false(t, p): return False
    cast_if_true = conditional_caster(always_true, fireball)
    cast_if_false = conditional_caster(always_false, fireball)
    print(f"True condition: {cast_if_true(target, power)}")
    print(f"False condition: {cast_if_false(target, power)}")
    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, fireball])
    print(f"Sequence results: {sequence(target, power)}")
