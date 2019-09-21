# selection sort template


def find_min_number(l: list) -> int:
    m = l[0]
    for a in l:
        if m > a:
            m = a

    return m


def selection_sort(l: list):
    sorted_list = []
    i = 1
    while i < len(l):
        # find min number
        # remove from original list
        # insert to sorted list
        i = i + 1

    return sorted_list

if __name__ == "__main__":
    l = [3, 7, 8, 5, 2, 1, 5, 9, 4]
    print(find_min_number(l))
    selection_sort(l)
    print(l)
