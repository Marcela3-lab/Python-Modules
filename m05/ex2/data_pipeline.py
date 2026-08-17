from abc import ABC, abstractmethod
from typing import Any, Union
from typing import Protocol

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
            
class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...

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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            data = processor.output(nb)
            plugin.process_output(data)


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        valores = [valor for (_, valor) in data]
        linha = ",".join(valores)
        print(f"CSV Output: {linha}")

class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pares = [f'"item_{idx}": "{valor}"' for (idx, valor) in data]
        json_str = "{" + ", ".join(pares) + "}"
        print(f"JSON Output: {json_str}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print(" ")
    print(" ")
    print("Initialize Data Stream...")
    data = DataStream()
    data.process_stream(3)
    print(" ")
    print(" ")
    print("Registering Processors")
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
    data.register_processor(text)
    data.register_processor(log)
    
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
