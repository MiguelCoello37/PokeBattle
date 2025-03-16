from pb_pokeapi.pokeapi_move import PokeApiMove


def create_pokeapi_move(data: dict):
    name = data.get("name")
    type = data.get("type").get("name")
    power = data.get("power")
    pp = data.get("pp")
    accuracy = data.get("accuracy")
    priority = data.get("priority")
    target = data.get("target").get("name")
    category = data.get("category")
    damage_class = data.get("damage_class").get("name")
    effect_chance = data.get("effect_chance")
    description = data.get("description")
    effect = data.get("effect")
    effect_changes = data.get("effect_changes")
    effect_entries = data.get("effect_entries")
    flavor_text_entries = data.get("flavor_text_entries")

    return PokeApiMove(name, power, pp, accuracy, type, category, description, priority, target, damage_class, effect_chance, effect, effect_changes, effect_entries, flavor_text_entries)
