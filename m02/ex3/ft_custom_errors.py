class GardenError (Exception):
    def __init__(self,message = "Caught"):


class PlantError(GardenError):
    super.__init__(self,)
    def test_garden_error():
        raise GardenError("The tomato plant is wilting!")


class WaterError(GardenError):
    def test_garden_error():
        raise WaterError("Not enough water in the tank!")


print("=== Custom Garden Error Demo ===")
print("Testing PlantError")
print(f"Caught PlantError: {PlantError.test_garden_error()}")

print("Testing WaterError")
print(f"Caught WaterError: {PlantError.test_garden_error()}")


print("Testing  catching all garden errors...")
print(f"Caught GardenErro: {}")


# if __name__ == "__main__":
#     try:
#         a = 3
#         b = 0
#         if b == 0:
#             raise DeuRuimError("Mensagem")
#     except DeuRuimError as e:
#         print(e)
#     except Exception:
#         print(Exception.__str__)