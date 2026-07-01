class PlantError(Exception):
    pass


def water_plant(plant_name) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant namo to water '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    print("Opening watering system")

    try:
        plants = ["Tomato", "Lettuce", "Carrots"]
        for plant in plants:
            water_plant(plant)

    except PlantError as e:
        print(f"Caught PlantError {e}")
        print("... ending tests and returning to main")
        return

    finally:
        print("Closing watering system")
    print()
    print("Testing invalid plants...")

    print("Opening watering system")

    try:
        plants = ["Tomato", "lettuce", "Carrots"]

        for plant in plants:
            water_plant(plant)

    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("... ending tests and returning to main")
        return

    finally:
        print("Closing watering system")
        print()
        print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
