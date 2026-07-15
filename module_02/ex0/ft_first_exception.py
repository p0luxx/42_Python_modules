#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    valid_input = "25"
    invalid_input = "abc"
    print("=== Garden Temperature ===\n")
    print(f"Input data is '{valid_input}'")
    try:
        temp = input_temperature(valid_input)
        print(f"Temperature is now {temp}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print(f"Input data is '{invalid_input}'")
    try:
        input_temperature(invalid_input)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
