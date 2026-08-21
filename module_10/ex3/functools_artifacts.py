import functools
import operator
from typing import Callable, Any, List


def spell_reducer(spells: List[int], operation: str) -> int:
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    if operation not in operations:
        raise ValueError(f"Operación desconocida: {operation}")

    return functools.reduce(operations[operation], spells)


def partial_enchanter(
                        base_enchantment: Callable[[int, str, str], str]
                     ) -> dict[str, Callable[[str], str]]:
    return {
        "flame": functools.partial(base_enchantment, 50, "Flaming"),
        "frost": functools.partial(base_enchantment, 50, "Frozen"),
        "lightning": functools.partial(base_enchantment, 50, "Lightning")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n debe ser un número entero no negativo")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"
    return cast


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells_power = [10, 20, 40, 30]
    print(f"Sum: {spell_reducer(spells_power, 'add')}")
    print(f"Product: {spell_reducer(spells_power, 'multiply')}")
    print(f"Max: {spell_reducer(spells_power, 'max')}")
    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(3.14))
