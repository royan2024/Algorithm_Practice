def binary_search(l: list, v: int):
    smallest_idx = 0
    largest_idx = len(l) - 1

    while smallest_idx <= largest_idx:
        idx = (largest_idx + smallest_idx) // 2
        if l[idx] < v:
            smallest_idx = idx + 1
        else:
            largest_idx = idx - 1

    return smallest_idx

if __name__ == "__main__":
    l = []
    while True:
        v = int(input("Enter a number: "))
        idx = binary_search(l, v)
        l.insert(idx, v)
        print(l)