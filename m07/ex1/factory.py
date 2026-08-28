from ex0.factory import CreatureFactory
from . import creature


class HealingCreatureFactory(CreatureFactory):
    def creat_base(self) -> creature.Sproutling:
        return creature.Sproutling()

    def creat_evolved(self) -> creature.Bloomelle:
        return creature.Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def creat_base(self) -> creature.Shiftling:
        return creature.Shiftling()

    def creat_evolved(self) -> creature.Morphagon:
        return creature.Morphagon()
