def input_temperature(temp_str: str) -> int:
    numero = int(temp_str)
    return numero


def test_temperature() -> None:
    input1 = 25
    input2 = "abc"
    try:
        temperaturavalida = input_temperature(str(input1))
        print(f"Input data is {input1}")
        print(f"Temperature is now {temperaturavalida}°C")
    except ValueError:
        print(f"Input data is {input1}")
        print("Caught input_temperature error: invalid "),
        (f"literal for int() with base 10: '{input1}'")
    print()
    try:
        print(f"Input data is {input2}")
        temperaturainvalida = input_temperature(input2)
        print(f"Temperature is now {temperaturainvalida}°C")
    except ValueError:
        print(
            "Caught input_temperature error: invalid "
            f"literal for int() with base 10: '{input2}'\n")
    finally:
        print("All tests completed - program didn't crash!")


print("=== Garden Temperature ===")
test_temperature()
