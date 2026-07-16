#!/usr/bin/python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown GardenError") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown PlantError") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if (plant_name == plant_name.capitalize()):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plants: list) -> None:
    print("Opening watering system")
    try:
        for i in plants:
            water_plant(i)
    except GardenError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    valid = ["Tomato", "Lettuce", "Carrots"]
    no_valid = ["Tomato", "lettuce"]
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    test_watering_system(valid)
    print("Testing invalid plants...")
    test_watering_system(no_valid)
    print("Cleanup always happens, even with errors!")
