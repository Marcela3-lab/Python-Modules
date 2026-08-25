from ex0.factory import CreatureFactory
from . import creature


class HealingCreatureFactory(CreatureFactory):
    def creat_base(self):
        return creature.Sproutling()

    def creat_evolved(self):
        return creature.Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def creat_base(self):
        return creature.Shiftling()

    def creat_evolved(self):
        return creature.Morphagon()
