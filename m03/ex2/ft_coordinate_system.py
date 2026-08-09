import math

def get_player_pos() -> tuple[float, float, float]:
    while True:
        x = input("Digite a primeira cordenada: 'x':")
        y = input("Digite a segunda cordenada: 'y':")
        z = input("Digite a segunda cordenada: 'z':")

        if not x or not y or not z:
            print("Preencha todas cordenadas!")
            continue
        else:
            try:
                cx = float(x)
                cy = float(y)
                cz = float(z)
            except ValueError:
                print("Invalid syntax")
                continue
        return (cx, cy, cz)
if __name__ == "__main__":
    print("Get a first set of cordinates")
    pontos1 = get_player_pos()
    print(f"Got a first tuple: {pontos1}")
    x1 = pontos1[0]
    y1 = pontos1[1]
    z1 = pontos1[2]
    print(f"It includes: X = {x1}, Y = {y1}, Z = {z1}")
    dist = math.sqrt(x1**2 + y1**2 + z1**2)
    print(f"Distância do centro (origem): {dist:.4f}")
    print()
    print("Get a seconde set of cordinates")
    pontos2 = get_player_pos()
    print(f"Got a seconde tuple: {pontos2}")
    x2 = pontos2[0]
    y2 = pontos2[1]
    z2 = pontos2[2]
    print(f"It includes: X = {x2}, Y = {y2}, Z = {z2}")
    distset = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distância entre os pontos: {distset:.4f}")