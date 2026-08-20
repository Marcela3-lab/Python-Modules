import dark_validator

def dark_spell_allowed_ingredients() -> list:
    lista: list = ["bats","frogs","arsenic","eyball"]
    return(lista)


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    res = dark_validator.validate_ingredients(ingredients)
    if "VALID" in res:
        return(f"Spell recorded: {spell_name} {ingredients}  - VALID")
    return("IGREDIENT NOT FOUND!!")