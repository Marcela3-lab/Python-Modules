def input_temperature(temp_str: str) -> int:
    numero = int(temp_str)
    if numero >= 0 & numero <= 40:
        return numero
    raise ValueError("Temperatura fora do interalor permitido")


def test_temperature() -> None:
    input1 = 25
    input2 = "abc"
    highvalue = 100
    lowvalue = -50
    try:
        print(f"Input data is {input1}")
        temperaturavalida = input_temperature(str(input1))
        print(f"Temperature is now {temperaturavalida}°C\n")
    except ValueError:
        print(f"Input data is {input1}")
        print(
            "Caught input_temperature error: invalid "
            f"literal for int() with base 10: '{input2}'\n")
    try:
        print(f"Input data is {input2}")
        temperaturainvalida = input_temperature(str(input2))
        print(f"Temperature is now {temperaturainvalida}°C\n")
    except ValueError:
        print(
            "Caught input_temperature error: invalid "
            f"literal for int() with base 10: '{input2}'\n")
    try:
        print(f"Input data is {highvalue}")
        temperaturainvalida = input_temperature(str(highvalue))
        print(f"Temperature is now {temperaturainvalida}°C\n")
    except ValueError:
        print(
            "Caught input_temperature error: invalid "
            f"literal for int() with base 10: '{input2}'\n")
    try:
        print(f"Input data is {lowvalue}")
        temperaturainvalida = input_temperature(str(lowvalue))
        print(f"Temperature is now {temperaturainvalida}°C\n")
    except ValueError:
        print(
            "Caught input_temperature error: invalid "
            f"literal for int() with base 10: '{input2}'\n")
    finally:
        print("All tests completed - program didn't crash!")


print("=== Garden Temperature ===")
test_temperature()
