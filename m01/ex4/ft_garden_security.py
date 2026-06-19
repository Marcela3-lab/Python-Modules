class Plant:
    def __init__(self, name, height=0, age=0):
        self.name = name
        self._height = height
        self._age = age

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, height):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False

        self._height = height
        return True

    def set_age(self, age):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False

        self._age = age
        return True


print("=== Garden Security System ===")

plant1 = Plant("Rose", 15.0, 10)

print(
    f"Plant created: {plant1.name}: "
    f"{plant1.get_height()}cm, "
    f"{plant1.get_age()} days old"
)

plant1.set_height(25)
print("Height updated: 25cm")

plant1.set_age(30)
print("Age updated: 30 days")

if not plant1.set_height(-5):
    print("Height update rejected")

if not plant1.set_age(-10):
    print("Age update rejected")

print(
    f"Current state: {plant1.name}: "
    f"{plant1.get_height()}cm, "
    f"{plant1.get_age()} days old"
)
