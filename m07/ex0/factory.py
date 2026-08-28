from abc import ABC, abstractmethod
from . import creature


class CreatureFactory(ABC):
    @abstractmethod
    def creat_base(self) -> creature.Creature:
        ...

    @abstractmethod
    def creat_evolved(self) -> creature.Creature:
        ...


class FlameFactory(CreatureFactory):
    def creat_base(self) -> creature.Flameling:
        return creature.Flameling()

    def creat_evolved(self) -> creature.Pyrodon:
        return creature.Pyrodon()


class AquaFactory(CreatureFactory):
    def creat_base(self) -> creature.Aquabub:
        return creature.Aquabub()

    def creat_evolved(self) -> creature.Torragon:
        return creature.Torragon()
