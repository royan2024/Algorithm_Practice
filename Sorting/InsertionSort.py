# insertion sort template


def insertion_sort(l: list) -> list:
    sorted_list = []
    i = 0
    while i < len(l):
        x = l[i]
        # TODO: x가 sorted list의 어디에 들어가야 하나?
        # how-1: sorted list를 앞에서부터 보고, x보다 큰 값이 나오는 위치에 x를 insert
        idx = len(sorted_list)
        for j in range(len(sorted_list)):
            y = sorted_list[j]
            if y > x:
                idx = j
                break
        sorted_list.insert(idx, x)
        print(sorted_list)
        # how-2: sorted list를 binary search하고 맞는 위치에 x를 insert
        i = i + 1

    return sorted_list


if __name__ == "__main__":
    l = [3, 7, 8, 5, 2, 1, 5, 9, 4]
    l = insertion_sort(l)
    print(l)
