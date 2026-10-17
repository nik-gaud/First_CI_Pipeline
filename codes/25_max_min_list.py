def find_max_min(numbers):
    if len(numbers) == 0:
        raise ValueError("List is empty")
    maximum = numbers[0]
    minimum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return (maximum, minimum)


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Max and Min:", find_max_min(nums))