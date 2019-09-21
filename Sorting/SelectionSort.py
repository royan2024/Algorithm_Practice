# selection sort template


def selection_sort(l: list):
    sorted_list = []
    i = 1
    while i < len(l):
        number = 0
        for a in l:
            if a > number:
                sorted_list.append(a)
            else:
                sorted_list.insert(0, a)
            a = number


    ##### YOUR CODE HERE #####
    # selection sort는 실제로 list를 안에서 바꾸면 되기 때문에
    # 따로 리턴을 할 필요가 없습니다
    ##########################


if __name__ == "__main__":
    l = [3, 7, 8, 5, 2, 1, 5, 9, 4]
    selection_sort(l)
    print(l)
