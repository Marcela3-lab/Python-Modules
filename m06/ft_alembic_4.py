import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.creat_air()}")
print("Now show that not all functions can be reached")
print("This will raise an exception!")
try:
    print(alchemy.creat_earth())
except ArithmeticError as e:
    print(e)
