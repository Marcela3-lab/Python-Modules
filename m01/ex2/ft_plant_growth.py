class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.agee = age

    def grow(self):
        self.height += 0.8

    def age(self):
        self.agee += 1


plant = Plant("Rose", 25.0, 30)
grow_init = plant.height
print("=== Garden Plant Growth ===")
for i in range(7):
    print("=== Day 1 ===")
    print(f"{plant.name}: {round(plant.height,1)}cm, {plant.agee} days old")
    plant.grow()
    plant.age()
res = plant.height - grow_init
print(f"Growth this week: {round(res,1)}")
