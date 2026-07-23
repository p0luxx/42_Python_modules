#!/usr/bin/python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[str] = []
        self.rank: int = 0

    def validate(self, data: Any) -> bool:
        pass

    def ingest(self, data: Any) -> None:
        pass

    def output(self, data: Any) -> tuple[int, str]:
        if not self.storage:
            raise Exception("No data to output")
        data = self.storage.pop
        value = self.rank - (len(self.storage) - 1)
        return (value, data)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, int) or isinstance(data, float):
            return True
        else:
            return False

    def ingest(self, data: [int, float]) -> None:
        if self.validate(data):
            self.storage += data
        else:
            print("Test invalid ingestion of string 'foo' "
                  "without prior validation:")
            raise Exception("Got exception: Improper numeric data")


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        pass


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    num = 42.2
    text = "hello"
    process0 = NumericProcessor()
    process0.ingest(num)
    process1 = NumericProcessor()
    print(f"Trying to validate input '{num}': ", process0)
    print(f"Trying to validate input '{text}': ", process1)
