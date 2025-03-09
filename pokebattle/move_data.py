from dataclasses import dataclass


@dataclass(frozen=True)
class MoveData:
    name: str
