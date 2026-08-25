from abc import ABC, abstractmethod
from ex1 import capability


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature):
        return True

    def act(self, creature):
        return creature.attack()


class AggressiveStrategy():
    def is_valid(self, creature):
        return isinstance(creature, capability.TransformCapability())

    def act(self, creature):
        if not self.is_valid(creature):
            raise ValueError("Creature cannot use AggressiveStrategy")
        return (
            creature.transform(),
            creature.attack(),
            creature.revert()
                    )


class DefensiveStrategy():
    def is_valid(self, creature):
        return isinstance(creature, capability.HealCapability())

    def act(self, creature):
        if not self.is_valid(creature):
            raise ValueError("Creature cannot use DefensiveStrategy")
        return (
            creature.attack(),
            creature.heal()
        )
