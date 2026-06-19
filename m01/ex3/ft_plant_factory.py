class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"Created: {self.name}{self.height}{self.age}")


print("=== Plant Factory Output ===")
plant1 = Plant("Rose: ", "25.0cm, ", "30 days old")
plant2 = Plant("Oak: ", "200.0cm, ", "365 days old")
plant3 = Plant("Cactus: ", "5.0m, ", "90 days old")
plant4 = Plant("Sunflower: ", "80.0cm, ", "45 days old")
plant5 = Plant("Fern: ", "15.0cm, ", "120 days old")

plant1.show()
plant2.show()
plant3.show()
plant4.show()
plant5.show()
