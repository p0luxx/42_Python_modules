#!/usr/bin/python3

from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str = "no_target") -> str: ...


class TransformCapability(ABC):
    def __init__(self, is_evolved: bool = False) -> None:
        self.is_evolved = False

    @abstractmethod
    def transform(self) -> str: ...

    @abstractmethod
    def revert(self) -> str: ...
