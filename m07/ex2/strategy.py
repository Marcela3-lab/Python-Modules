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
        return f"{creature.attack()}\n"


class AggressiveStrategy():
    def is_valid(self, creature):
        return isinstance(creature, capability.TransformCapability)

    def act(self, creature):
        if not self.is_valid(creature):
            raise ValueError("Creature cannot use AggressiveStrategy")
        return (
            f"{creature.transform()}\n"
            f"{creature.attack()}\n"
            f"{creature.revert()}\n"
                    )


class DefensiveStrategy():
    def is_valid(self, creature):
        return isinstance(creature, capability.HealCapability)

    def act(self, creature):
        if not self.is_valid(creature):
            raise ValueError("Creature cannot use DefensiveStrategy")
        return (
            f"{creature.attack()}\n"
            f"{creature.heal()}\n"
        )
