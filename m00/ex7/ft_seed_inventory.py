def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if unit == "packets":
        print(f"{seed_type} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type} seeds: {quantity} grams total")
    unit_text = "square meter" if quantity == 1 else "square meters"
    if unit == "area":
        print(f"{seed_type} seeds: covers {quantity} {unit_text}")
