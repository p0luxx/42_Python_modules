from abc import ABC, abstractmethod
from typing import Any
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[str] = []
        self.rank: int = 0
        self.total: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.storage:
            raise Exception("No data to output")
        data = self.storage.pop(0)
        value = self.rank
        self.rank += 1
        return (value, data)

    def __str__(self) -> str:
        name = self.__class__.__name__
        return "".join([" " + c if c.isupper() and i > 0 else c
                       for i, c in enumerate(name)])


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) in (int, float):
            return True
        if isinstance(data, list):
            if not data:
                return False
            return all(type(item) in (int, float) for item in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self.storage.append(str(item))
                self.total += 1
        else:
            self.storage.append(str(data))
            self.total += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            if not data:
                return False
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper data")
        if isinstance(data, list):
            for item in data:
                self.storage.append(item)
                self.total += 1
        else:
            self.storage.append(data)
            self.total += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(k, str) and isinstance(v, str)
                       for k, v in data.items())
        if isinstance(data, list):
            if not data:
                return False
            for item in data:
                if not isinstance(item, dict):
                    return False
                if not all(isinstance(k, str) and isinstance(v, str)
                           for k, v in item.items()):
                    return False
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Invalid log")
        if isinstance(data, list):
            for item in data:
                formated_log = ": ".join(item.values())
                self.storage.append(formated_log)
                self.total += 1
        elif isinstance(data, dict):
            formated_log = ": ".join(data.values())
            self.storage.append(formated_log)
            self.total += 1


class DataStream():
    def __init__(self):
        self.processor_list: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if isinstance(proc, DataProcessor):
            if proc not in self.processor_list:
                self.processor_list.append(proc)
        else:
            raise Exception("Invalid processor added")

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            for proc in self.processor_list:
                if proc.validate(item):
                    proc.ingest(item)
                    break

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.processor_list) == 0:
            print("No processor found, no data")
        for proc in self.processor_list:
            print(f"{proc}: total {proc.total} items processed, "
                  f"remaining {len(proc.storage)} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    bigpapi = DataStream()
    bigpapi.print_processors_stats()
    print()

    mixed_stream = [
        42,
        [3.14, -1.0, 2.718],
        "Hello world",
        ["Python", "C", "POO"],
        {"level": "INFO", "msg": "Boot OK"},
        [
            {"status": "200", "path": "/home"},
            {"status": "404", "path": "/missing"}
        ]
    ]
    print("Registering Processors...")
    n_processor = NumericProcessor()
    t_processor = TextProcessor()
    l_processor = LogProcessor()
    bigpapi.register_processor(n_processor)
    bigpapi.register_processor(t_processor)
    bigpapi.register_processor(l_processor)
    print("Processing mixed stream...\n")
    bigpapi.process_stream(mixed_stream)
    print("--- Stats after ingest ---")
    bigpapi.print_processors_stats()
    print()
    print("Consuming 1 item from NumericProcessor...")
    print("Extracted:", n_processor.output())
    print()
    print("--- Stats after output ---")
    bigpapi.print_processors_stats()
