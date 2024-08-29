from dataclasses import dataclass


@dataclass
class InputData:
    @dataclass
    class InputEntity:
        key: str
        name: str
        duties: list[str]

    data: list[InputEntity]
    extra: dict[str, str] = None


@dataclass
class OutputData:
    @dataclass
    class OutputEntity:
        name: str
        duty: str

    data: list[list[OutputEntity]]
    extra: dict[str, str] = None
