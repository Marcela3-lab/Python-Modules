import sys

print("=== Command Quest ===")


def verify_arguments() -> None:
    count_arg = 1
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argument) == 0:
        print("No arguments provided!")
        print("Total arguments: 1")
        return
    print(f"Arguments received: {len(sys.argv)}")
    while count_arg <= len(sys.argv):
        print(f"Arguments {count_arg}: {sys.argv[count_arg]}")
        count_arg = count_arg + 1
    print(f"Total arguments: {len(sys.argv)}")
