from ex0.creature import Creature
from .capability import HealCapability, TransformCapability

class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling","Grass")
    def attack(self):
        return ("Sproutling uses Vine Whip!")
    def heal(self, target=None):
        return "Sproutling heals itself for a small amount"

class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle","Grass/Fairy")
    def attack(self):
        return ("Bloomele uses Petal Dance!")
    def heal(self, target=None):
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):

    def __init__(self):
        super().__init__("Shiftling", "Normal")
        self.transformed = False

    def attack(self):
        if self.transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self):
        self.transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self):
        self.transformed = False
        return "Shiftling returns to normal."


    
class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon","Normal/Dragon")
        self.transformed = False
    def attack(self):
        if self.transformed:
            return("Morphagon unleashes a devastating morph strike!")
        return("Morphagon attacks normally.")
    def transform(self):
        self.transformed = True
        return "Morphagon morphs into a dragonic battle form!"
    def revert(self):
        self.transformed = False
        return ("Morphagon stabilizes its form.")    

