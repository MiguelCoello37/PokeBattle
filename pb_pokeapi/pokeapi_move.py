from dataclasses import dataclass


@dataclass(frozen=True)
class PokeApiMove:
    name: str
    power: int
    pp: int
    accuracy: int
    type: str
    category: str
    description: str
    priority: int
    target: str
    damage_class: str
    effect_chance: int
    effect: str
    effect_changes: str
    effect_entries: str
    flavor_text_entries: str
    