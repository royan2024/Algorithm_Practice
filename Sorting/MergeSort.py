def merge(left, right):
    merged_list = []
    i = 0 # for left
    j = 0 # for right
    for _ in range(len(left) + len(right)):
        if i == len(left):
            merged_list.append(right[j])
            j = j + 1
        elif j == len(right):
            merged_list.append(left[i])
            i = i + 1
        elif left[i] < right[j]:
            merged_list.append(left[i])
            i = i + 1
        else:
            merged_list.append(right[j])
            j = j + 1
    return merged_list


def merge_sort(l:list):
    first = []
    second = []
    if len(l) <= 1:
        return l
    elif len(l) > 1:
        idx = len(l) // 2
        first.extend(l[0:idx])
        second.extend(l[idx:len(l)])
        first = merge_sort(first)
        second = merge_sort(second)
        return merge(first, second)






    # 아닌 경우, 반으로 나눠서 merge sort를 수행시키고
    # 나온 결과를 merge함수에 넣어줍니다


if __name__ == "__main__":
    print(merge([1, 3, 5, 6], [2, 4, 7, 8]))
    print(merge_sort([6, 5, 3, 1, 8, 7, 2, 4, 5]))
