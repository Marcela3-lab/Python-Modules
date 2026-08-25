from abc import ABC, abstractmethod
from . import creature


class CreatureFactory(ABC):
    @abstractmethod
    def creat_base(self):
        ...

    @abstractmethod
    def creat_evolved(self):
        ...


class FlameFactory(CreatureFactory):
    def creat_base(self):
        return creature.Flameling()

    def creat_evolved(self):
        return creature.Pyrodon()


class AquaFactory(CreatureFactory):
    def creat_base(self):
        return creature.Aquabub()

    def creat_evolved(self):
        return creature.Torragon()
