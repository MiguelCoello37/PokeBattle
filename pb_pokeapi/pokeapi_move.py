from dataclasses import dataclass


@dataclass(frozen=True)
class PokeApiMove:
    name: str
    url: str
