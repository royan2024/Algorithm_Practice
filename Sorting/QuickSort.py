def partition(A: list, lo: int, hi: int) -> int:
    pivot = A[hi]
    i = lo
    for j in range(lo, hi):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i = i + 1
    A[i], A[hi] = A[hi], A[i]
    # pivot이 들어갈 위치
    return i


def quick_sort(A: list, lo: int, hi: int):
    if lo < hi:
        p = partition(A, lo, hi)
        quick_sort(A, lo, p - 1)
        quick_sort(A, p + 1, hi)


if __name__ == "__main__":
    l = [3, 7, 8, 5, 2, 1, 5, 9, 4]
    quick_sort(l, 0, len(l) - 1)
    print(l)
