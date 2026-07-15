#!/usr/bin/python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown GardenError") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown PlantError") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown WaterError") -> None:
        super().__init__(message)


def simulate_garden(code: int) -> None:
    if code == 0:
        raise PlantError("The tomato plant is wilting!")
    elif code == 1:
        raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        simulate_garden(0)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    print("Testing WaterError...")
    try:
        simulate_garden(1)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    try:
        simulate_garden(0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        simulate_garden(1)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly!")
