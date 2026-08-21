from .. import elements
from alchemy import potions
import elements as alchemy_elements


def lead_to_gold() -> str:
    air = elements.creat_air()
    strength = potions.strength_potion()
    fire = alchemy_elements.creat_fire()

    return (f"Recipe transmuting Lead to Gold: brew {air} and "
            f"{strength} mixed with {fire}")
