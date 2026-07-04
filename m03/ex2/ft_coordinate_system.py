import math


def get_player_pos() -> tuple[float, ...]:
    while True:
        pos = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = pos.split(",")
        if len(parts) != 3:
            print("You must enter 3 values.")
            continue
        coords = []
        try:
            for part in parts:
                coords.append(float(part))
        except ValueError:
            print(f"Error: '{part}' is not a valid float.")
            continue
        x, y, z = coords
        print(f"Got a first tuple: {coords}")
        print(f"It includes: X={x}, Y={y}, Z={z}")

        distance = math.sqrt(x**2 + y**2 + z**2)
        print(f"Distance to center: {distance:.4f}")
        return (x, y, z)


def second_set() -> tuple[float, ...]:
    while True:
        pos = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = pos.split(",")
        if len(parts) != 3:
            print("You must enter 3 values.")
            continue
        coords = []
        try:
            for part in parts:
                coords.append(float(part))
        except ValueError:
            print(f"Error: '{part}' is not a valid float.")
            continue
        x, y, z = coords
        return (x, y, z)


if __name__ == "__main__":
    print("Get a first set of cordinates")
    pontos = get_player_pos()
    print()
    print("Get a second set of cordinates")
    pontos = pontos + second_set()
    dx = pontos[0] - pontos[3]
    dy = pontos[1] - pontos[4]
    dz = pontos[2] - pontos[5]
    distancia_d = math.sqrt(dx**2 + dy**2 + dz**2)
    print()
    print(f"Distance between the 2 sets of coordinates {round(distancia_d,4)}")
