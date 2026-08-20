from .. import elements
from alchemy import potions
import elements as alchemy_elements
def lead_to_gold() -> str:
    return(f"Recipe transmuting Lead to Gold: brew {elements.creat_air()} and {potions.strength_potion()} mixed with {alchemy_elements.creat_fire()}")
