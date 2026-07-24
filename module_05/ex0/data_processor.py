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

    def ingest(self, data: Any) -> None:
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

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper data")
        if isinstance(data, list):
            for item in data:
                self.storage.append(item)
        else:
            self.storage.append(data)


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
        elif isinstance(data, dict):
            formated_log = ": ".join(data.values())
            self.storage.append(formated_log)


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    num = 42
    text = "Hello"
    process0 = NumericProcessor()
    print(f" Trying to validate input '{num}': {process0.validate(num)}")
    print(f" Trying to validate input '{text}': {process0.validate(text)}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        process0.ingest("foo")
    except Exception as e:
        print(f" Got exception: {e}")
    data_list = [1, 2, 3, 4, 5]
    print(f" Processing data: {data_list}")
    process0.ingest(data_list)
    print(" Extracting 3 values...")
    for i in range(0, 3):
        rank, value = process0.output()
        print(f" Numeric value {rank}: {value}")
    print("\nTesting Text Processor...")
    texting = TextProcessor()
    print(f" Trying to validate input '{num}': {texting.validate(num)}")
    text_list = ['Hello', 'Nexus', 'World']
    texting_procesor = TextProcessor()
    texting_procesor.ingest(text_list)
    print(f" Processing data: {text_list}")
    print(" Extracting 1 value...")
    for _ in range(1):
        rank, value = texting_procesor.output()
        print(f" Text value {rank}: {value}")
    example = [
                {'log_level': 'NOTICE', 'log_message':
                    'Connection to server'},
                {'log_level': 'ERROR', 'log_message':
                    'Unauthorized access!!'}]
    processor_logs = LogProcessor()
    print("\nTesting Log Processor...")
    print(
            f" Trying to validate input '{text}': "
            "{processor_logs.validate(text)}"
        )
    print(f" Processing data: {example}")
    processor_logs.ingest(example)
    for _ in range(2):
        rank, value = processor_logs.output()
        print(f" Log entry {rank}: {value}")
