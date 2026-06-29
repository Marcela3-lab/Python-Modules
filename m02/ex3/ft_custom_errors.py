class GardenError (Exception):
    def __init__(self, message = ""):
        ...


class PlantError(GardenError):
    def __init__(self):
        ...


class WaterError(GardenError):
    def __init__(self):
        ...



#class DeuRuimError(Exception):
#     def __str__(self):
#         return "Batata"


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