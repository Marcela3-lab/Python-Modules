def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        res = int('abc')
    elif operation_number == 1:
        res = 3/0
    elif operation_number == 2:
        res = open("a", "r")
    elif operation_number == 3:
        res = 'a' + 3
    else:
        return
    return res


def test_error_types() -> None:
    for input in range(0, 4):
        try:
            garden_operations(input)
        except BaseException as error_message:
            print(error_message)


if __name__ == "__main__":
    test_error_types()
