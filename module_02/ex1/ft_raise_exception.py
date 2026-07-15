#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    integer = int(temp_str)
    if integer >= 0 and integer <= 40:
        return integer
    elif integer > 40:
        raise ValueError(f"{integer}°C is too hot for plants (max 40°C)")
    else:
        raise ValueError(f"{integer}°C is too cold for plants (min 0°C)")


def test_temperature() -> None:
    valid_input = "25"
    invalid_input = "abc"
    hot = "100"
    cold = "-50"
    print("=== Garden Temperature Checker ===\n")
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
    print(f"\nInput data is '{hot}'")
    try:
        input_temperature(hot)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print(f"\nInput data is '{cold}'")
    try:
        input_temperature(cold)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
