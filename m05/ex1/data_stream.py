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

class DataStream():
    def __init__ (self)->None:
            self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
            self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        if len(self.processors) == 0:
            print("No processor found, no data")
            return
        for item in stream:
            encontrado = False
            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    encontrado = True
                    break;
            if not encontrado:
                print(f"DataStream error - Can't process element in stream: {item}")
    
    def print_processors_stats(self) -> None:
            for proc in self.processors:
                nome = type(proc).__name__.replace("Processor", " Processor")
                restant = len(proc.dados)
                total = proc.rank + len(proc.dados)
                print(f"{nome}: total {total} items processed, remaining {restant} on processor")

if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print(" ")
    print(" ")
    print("Initialize Data Stream...")
    data = DataStream()
    stream = ['k']
    

    print("== DataStream c ==")
    data.process_stream(stream)
    print(" ")
    print(" ")
    print("Resgistering Numeric Processor")
    print(" ")
    print(" ")
    print(
    "Send first batch of data on stream: "
    "['Hello world', [3.14, -1, 2.71], "
    "[{'log_level': 'WARNING', "
    "'log_message': 'Telnet access! Use ssh instead'}, "
    "{'log_level': 'INFO', "
    "'log_message': 'User wil is connected'}], "
    "42, ['Hi', 'five']]"
)
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    data.register_processor(numeric)
    
    stream = [
    "Hello world",
    [3.14, -1, 2.71],
    [
        {"log_level": "WARNING", "log_message": "Telnet access! Use ssh instead"},
        {"log_level": "INFO", "log_message": "User wil is connected"},
    ],
    42,
    ["Hi", "five"],
]
    data.process_stream(stream)
    print("== DataStream statistics ==")
    data.print_processors_stats()
    print(" ")
    print(" ")
    print("Registering other data processors")
    print("Send the same batch again")
    print("== DataStream statistics ==")

    stream = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    data.register_processor(text)
    data.register_processor(log)
    data.process_stream(stream)
    data.print_processors_stats()
    print("Consume smoe elements from the data processors: Numeric: 3, Text 2, Log 1")
    print("== DataStream statistics ==")
    print(" ")
    print(" ")
   
    for _ in range(3):
        numeric.output()

    for _ in range(2):
        text.output()

    for _ in range(1):
        log.output()

    data.print_processors_stats()