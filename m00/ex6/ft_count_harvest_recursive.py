def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))

    def helper(indice):
        if indice <= day:
            print("Day", indice)
            helper(indice + 1)
    helper(1)
    print("Harvest time!")
