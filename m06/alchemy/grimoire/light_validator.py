from . import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spellbook.light_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()
    for item in allowed:
        if item.lower() in ingredients_lower:
            return (f"{ingredients_lower} - VALID")
    return (f"{ingredients_lower} - INVALID")
