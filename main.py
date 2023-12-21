from function import add, mult

if __name__ == '__main__':

    # assert function add
    assert add(1, 1) == 2
    assert add(1, 2) == 3
    assert add(1, 3) == 4

    # assert function sub
    assert mult(2, 1) == 2
    assert mult(3, 1) == 3
    assert mult(4, 1) == 4


    a, b = map(int, input('a & b: ').split())

    print(f'result: {add(a, b)}')
    print(f'result: {mult(a, b)}')