class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}{self.height}{self.age}")


print("=== Garden Plant Registry ===")
plant1 = Plant("Rose: ", "25 cm, ", "30 days old")
plant2 = Plant("Sunflower: ", "80 cm, ", "45 days old")
plant3 = Plant("Cactus: ", "15 cm, ", "120 days old")

plant1.show()
plant2.show()
plant3.show()
