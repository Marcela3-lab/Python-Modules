from abc import ABC, abstractmethod

class HealCapability(ABC):

    @abstractmethod
    def heal(self, target=None):
        ...

class TransformCapability(ABC):
    def __init__(self):
        self.transformed = False
    @abstractmethod
    def transform(self):
        ...
    @abstractmethod
    def revert(self):
        ...