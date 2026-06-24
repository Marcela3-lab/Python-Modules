class Plant():
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.age_days += 1


plant = Plant("Rose", 25.0, 30)
grow_init = plant.height
print("=== Garden Plant Growth ===")
for i in range(1, 8):
    print(f"=== Day {i} ===")
    print("{}: {}cm, {} days old".format(
        plant.name,
        round(plant.height, 1),
        plant.age_days
    ))

    plant.grow()
    plant.age()
res = plant.height - grow_init
print(f"Growth this week: {round(res, 1)}")
