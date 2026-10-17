def decimal_to_binary(number):
    if number < 0:
        raise ValueError("Negative numbers are not allowed")
    if number == 0:
        return "0"
    result = ""
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    return result


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Binary:", decimal_to_binary(num))