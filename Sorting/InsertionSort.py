# insertion sort template


def insertion_sort(l: list) -> list:
    sorted_list = []
    i = 1
    while i < len(l):
        a = i
        while a > 0 and l[a - 1] > l[a]:
            l[a - 1], l[a] = l[a], l[a - 1]
            a = a - 1
            sorted_list = l
        i = i - 1



    return sorted_list


if __name__ == "__main__":
    l = [3, 7, 8, 5, 2, 1, 5, 9, 4]
    l = insertion_sort(l)
    print(l)
