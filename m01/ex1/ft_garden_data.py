class Plant:
    def __init__(self, name: str, height: str, age: str) -> None:
        self.name: str = name
        self.height: str = height
        self.age: str = age

    def show(self) -> None:
        print(f"{self.name}{self.height}{self.age}")


print("=== Garden Plant Registry ===")

plant1 = Plant("Rose: ", "25 cm, ", "30 days old")
plant2 = Plant("Sunflower: ", "80 cm, ", "45 days old")
plant3 = Plant("Cactus: ", "15 cm, ", "120 days old")

plant1.show()
plant2.show()
plant3.show()
