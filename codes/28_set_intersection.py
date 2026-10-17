def set_intersection(first, second):
    result = set()
    for item in first:
        if item in second:
            result.add(item)
    return result


if __name__ == "__main__":
    a = set(map(int, input("Enter first set: ").split()))
    b = set(map(int, input("Enter second set: ").split()))
    print("Intersection:", set_intersection(a, b))