def get_nod(a, b):
    if a != 0 and b != 0:
        if a <= b:
            return get_nod(a, b % a)
        else:
            return get_nod(a % b, b)
    else:
        return a + b


def get_nok(a, b):
    return a * b / get_nod(a, b)


def get_nok(a, b, nod):
    return a * b / nod


if __name__ == '__main__':
    while 1:
        a = ''
        while not a:
            print("Enter value a: ", end='')
            a = input()
        a = int(a)
        b = ''
        while not b:
            print("Enter value b: ", end='')
            b = input()
        b = int(b)
        nod = get_nod(a, b)
        print("nod: ", nod)
        print("nok: ", get_nok(a, b, nod))
