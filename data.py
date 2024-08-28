from dataclasses import dataclass


@dataclass
class InputData:
    key: str
    name: str
    duties: list[str]


@dataclass
class OutputData:
    name: str
    duty: str
