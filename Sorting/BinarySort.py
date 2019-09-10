from Sorting.BinarySearch import binary_search

def binary_sort(l: list) -> list:
    sorted_list = []
    for v in l:
        idx = binary_search(sorted_list, v)
        sorted_list.insert(idx, v)

    return sorted_list


if __name__ == "__main__":
    l = [4, 5, 8, 9, 1]
    print(binary_sort(l))