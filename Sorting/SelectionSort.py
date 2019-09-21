# selection sort template


def find_min_number(l: list) -> int:
    m = l[0]
    for a in l:
        if m > a:
            m = a

    return m


def selection_sort(l: list):
    sorted_list = []
    while len(l) > 0:
        # find min number
        m = find_min_number(l)
        # remove from original list
        l.remove(m)
        # insert to sorted list
        sorted_list.append(m)

    return sorted_list


def selection_sort_in_place(l: list):
    for i in range(len(l)):
        m = i
        for j in range(i, len(l)):
            if l[m] > l[j]:
                m = j
        l[m], l[i] = l[i], l[m]

if __name__ == "__main__":
    l = [3, 7, 8, 5, 2, 1, 5, 9, 4]
    selection_sort_in_place(l)
    print(l)
