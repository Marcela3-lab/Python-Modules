import dark_spellbook

def validate_ingredients(ingredients: str) -> str:
    ml = dark_spellbook.light_spell_allowed_ingredients()
    for item in len(ml):
        if ingredients.lower == item:
            return(f"{item} VALID")
    return (f"{item} INVALID")