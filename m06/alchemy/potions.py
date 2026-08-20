from .elements import creat_earth, creat_air
from elements import creat_water, creat_fire
def healing_potion() -> str:
    return(f"Healing potion brewed with {creat_earth()} and {creat_air()}")

def strength_potion() -> str:
    return(f"Strength potion brewed with {creat_fire()} and {creat_water()}")