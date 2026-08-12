from abc import ABC, abstractmethod
from typing import Any, Union

class DataProcessor(ABC):

    def __init__(self) -> None:
        self.dados: list[str] = []
        self.rank = 0
    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        valor = self.dados.pop(0)
        rank_atual = self.rank
        self.rank += 1
        return (rank_atual, valor)

class NumericProcessor(DataProcessor):
    def validate(self, data: Any) ->bool:
        if isinstance(data, (int, float)):
            return True
        if (isinstance(data, list)):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        return False
    def ingest(self, data: Union[int, float, list]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self.dados.append(str(item))
        else:
            self.dados.append(str(data))

class TextProcessor(DataProcessor):
    def validate(self, data: Any) ->bool:
        if isinstance(data, (str)):
            return True
        if (isinstance(data, list)):
            for item in data:
                if not isinstance(item, (str)):
                    return False
            return True
        return False
    def ingest(self, data: Union[str,list]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self.dados.append(item)
        else:
                self.dados.append(str(data))

class LogProcessor(DataProcessor):
    def validate(self, data):
        if isinstance(data, dict):
            for chave, valor in data.items():
                if not isinstance(chave, str) or not isinstance(valor, str):
                    return False
            return True
        if isinstance(data, list):
            for item in data:
                if not self.validate(item):
                    return False
            return True
        return False

    def ingest(self, data: Union[dict, list]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                texto = f"{item['log_level']}: {item['log_message']}"
                self.dados.append(texto)
        else:
            texto = f"{data['log_level']}: {data['log_message']}"
            self.dados.append(texto)


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print(" ")
    print(" ")
    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest('foo')
    except ValueError as e:
        print(f"Got exception: {e}")
    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1,2,3,4,5])
    print("Extracting 3 values...")
    for _ in range(3):
        rank, valor = numeric.output()
        print(f"Numeric value {rank}: {valor}")
    print(" ")
    print("Testing Text Processor...")
    text= TextProcessor()
    print(f"Trying to validate input '42': {text.validate(42)}")
    print(f"Processing data: {['Hello', 'Nexus', 'World']}")
    text.ingest(['Hello', 'Nexus', 'World'])
    print("Extracting 1 value...")
    for _ in range(1):
        rank, valor = text.output()
        print(f"Text value {rank}: {valor}")
    print(" ")
    print(" ")
    print("Testing Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    dados_log = [
    {"log_level": "NOTICE", "log_message": "Connection to server"},
    {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
                ]
    print(f"Processing data: {dados_log}")
    log.ingest(dados_log)

    print("Extracting 2 values...")
    for _ in range(2):
        rank, valor = log.output()
        print(f"Log entry {rank}: {valor}")