def is_armstrong(number):
    if number < 0:
        return False
    digits = str(number)
    power = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** power
    return total == number


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Armstrong:", is_armstrong(num))
    