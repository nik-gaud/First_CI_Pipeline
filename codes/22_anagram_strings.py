def is_anagram(first, second):
    a = first.replace(" ", "").lower()
    b = second.replace(" ", "").lower()
    if len(a) != len(b):
        return False
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    print("Anagram:", is_anagram(s1, s2))