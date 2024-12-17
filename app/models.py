from dataclasses import dataclass

@dataclass
class CommandArg:
    id: int
    title: str
    value: str


@dataclass
class Command:
    id: int
    title: str
    command: str
    working_dir: str
    args: [CommandArg]
