from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    def __init__(self) -> None:
        self.dados: list[str] = []
    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...
    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...
    @abstractmethod
    def output(self) -> tuple[int, str]:
        ...