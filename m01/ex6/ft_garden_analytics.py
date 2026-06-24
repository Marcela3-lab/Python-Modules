from __future__ import annotations


class Plant:
    def __init__(self, nome: str, height: float, age: int) -> None:
        self.name: str = nome
        self.height: float = height
        self.age: int = age
        self.stats: Plant.Stats = Plant.Stats()

    class Stats:
        def __init__(self) -> None:
            self._grow_call: int = 0
            self._age_call: int = 0
            self._show_call: int = 0
            self._shade_call: int = 0

        def inc_grow(self) -> None:
            self._grow_call += 1

        def inc_age(self) -> None:
            self._age_call += 1

        def inc_show(self) -> None:
            self._show_call += 1

        def inc_shade(self) -> None:
            self._shade_call += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_call} grow, "
                f"{self._age_call} age, "
                f"{self._show_call} show"
            )

    def age_plant(self, days: int) -> None:
        self.age += days
        self.stats.inc_age()

    @staticmethod
    def check_age(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> Plant:
        return cls("unknown", 0, 0)

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        self.stats.inc_show()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.bloomed: bool = False

    def bloom(self) -> None:
        self.bloomed = True

    def grow_flower(self, valor: float) -> None:
        self.height += valor
        self.stats.inc_grow()

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self.stats.inc_shade()

        self.stats.display()
        print(f"{self.stats._shade_call} shade")

        print("[asking the oak to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide."
        )

        print(f"[statistics for {self.name}]")
        self.stats.display()
        print(f"{self.stats._shade_call} shade")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")
