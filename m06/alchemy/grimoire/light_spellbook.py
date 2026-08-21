from . import light_validator


def light_spell_allowed_ingredients() -> list:
    lista: list = ["earth", "air", "fire", "water"]
    return (lista)


def light_spell_record(spell_name: str, ingredients: str) -> str:
    res = light_validator.validate_ingredients(ingredients)
    if res.endswith("- VALID"):
        return (f"Spell recorded: {spell_name} ({res})")
    return (f"Spell rejected: {spell_name} ({res})")
