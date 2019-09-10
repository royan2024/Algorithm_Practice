def test_list(l: list):
    l[0], l[-1] = l[-1], l[0]

def test_int(a, b):
    a, b = b, a

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    test_list(l)
    print(l)
    a = 10
    b = 5
    test_int(a, b)
    print(a, b)