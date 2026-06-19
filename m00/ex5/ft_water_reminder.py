def ft_water_reminde():
    time = int(input("Days since last watering: "))
    if time > 2:
        print("Water the plants!")
    else:
        print("Plants are fine.")
