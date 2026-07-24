#!/usr/bin/python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[str] = []
        self.rank: int = 0
    
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


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) in (int, float):
            return True
        if isinstance(data, list):
            if not data:
                return False
            return all(type(item) in (int, float) for item in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self.storage.append(str(item))
        else:
            self.storage.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            if not data:
                return False
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception ("Improper data")
        if isinstance(data, list):
            for item in data:
                self.storage.append(item)
        else:
            self.storage.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(k, str) and isinstance(v, str) for k, v in data.items())
        if isinstance(data, list):
            if not data:
                return False
            for item in data:
                if not isinstance(item, dict):
                    return False
                if not all(isinstance(k, str) and isinstance(v, str) for k, v in item.items()):
                    return False
            return True
        return False

    
    def ingest(self, data: list[dict] | dict) -> None:
        if not self.validate(data):
            raise Exception ("Invalid log")
        if isinstance(data, list):
            for item in data:
                formated_log = ": ".join(item.values())
                self.storage.append(formated_log)
        elif isinstance(data, dict):
            formated_log = ": ".join(data.values())
            self.storage.append(formated_log)


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print("Testing Numeric Processor...")

    num = 42
    text = "Hello"

    process0 = NumericProcessor()

    print(f"Trying to validate input '{num}': {process0.validate(num)}")
    print(f"Trying to validate input '{text}': {process0.validate(text)}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        process0.ingest("foo")
    except Exception as e:
        print(f"Got exception: {e}")

    data_list = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_list}")
    process0.ingest(data_list)

    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = process0.output()
        print(f"Numeric value {rank}: {value}")

    process1 = TextProcessor()
    process1.ingest(text)
    rank, value = process1.output()
    print(rank, value)




    # Un único log:
    un_log = {'log_level': 'NOTICE', 'log_message': 'Connection to server'}

    # O una lista de logs:
    varios_logs = [
    {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
    {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]

    logs = LogProcessor()
    logs.ingest(varios_logs)
    rank, value = logs.output()
    print(rank, value)
