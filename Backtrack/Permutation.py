import random

def random_guess():
    answers = []
    while True:
        l = list(range(1, 9))
        random_list = []

        while len(random_list) < 8:
            idx = random.randint(0, 7)
            selected = l[idx]
            if selected not in random_list:
                random_list.append(selected)

        ll = random_list[0] * 100 + random_list[1] * 10 + random_list[2]
        lr = random_list[3]
        rhs = random_list[4] * 1000 + random_list[5] * 100 + random_list[6] * 10 + random_list[7]
        if ll * lr == rhs:
            if [ll, lr, rhs] not in answers:
                answers.append([ll, lr, rhs])
                print("%d * %d = %d" % (ll, lr, rhs))
                if len(answers) ==2:
                    break

def check(l):
    ll = 0
    lr = 0
    rhs = 0

    size = len(l)
    for i in range(size):
        if i < size / 2 - 1:
            ll = ll * 10 + l[i]
        elif i < size / 2:
            lr = l[i]
        else:
            rhs = rhs * 10 + l[i]

    if ll * lr == rhs:
        print("%d * %d = %d" % (ll, lr, rhs))
        return True
    return False

def perm(size, max_number, check_func, l = None):
    if l is None:
        l = []
    if len(l) == size:
        check_func(l)
        return

    for a in range(max_number + 1):
        if a not in l:
            l.append(a)
            perm(size, max_number, check_func, l)
            l.remove(a)

password = int(input("Enter Password:"))
def make_pw():
    pw = []
    for i in range(10):
        for a in range(10):
            if a not in pw:
                pw.append(a)
                pw.remove(a)

def get_pw():
    guess = []
    for i in range(10):
        for a in range(10):
            if a not in guess:
                guess.append(a)
                guess.remove(a)
    if guess == password:
        print("CORRECT! %s" % guess)

def check_pw(l):
    pw = 0
    for x in l:
        pw = pw * 10 + x
    if pw == password:
        print(("CORRECT" + str(password)))

def get_pattern(guess):
    if guess[0] + guess[3] + guess[6] == guess[1] + guess[4] + guess[7] == guess[2] + guess[5] + guess[8] == guess[0] + guess[1] + guess[2] == guess[3] + guess[4] + guess[5] == guess[6] + guess[7] + guess[8] == guess[0] + guess[4] + guess[8] == guess[2] + guess[4] + guess[6]:
        print("CORRECT! %s" % guess)


perm(9, 9, get_pattern)
