from . import light_validator

def light_spell_allowed_ingredients() -> list:
    lista: list = ["earth","air","fire","water"]
    return(lista)


def light_spell_record(spell_name: str, ingredients: str) -> str:
    res = light_validator.validate_ingredients(ingredients)
    if "VALID" in res:
        return(f"Spell recorded: {spell_name} {ingredients}  - VALID")
    return("IGREDIENT NOT FOUND!!")