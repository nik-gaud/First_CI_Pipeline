def rotate_list(items, k):
    n = len(items)
    if n == 0:
        return []
    k = k % n
    if k == 0:
        return list(items)
    return items[-k:] + items[:-k]


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    k = int(input("Enter k: "))
    print("Rotated list:", rotate_list(nums, k))