from function import add

if __name__ == '__main__':

    assert add(1, 1) == 2
    assert add(1, 2) == 3
    assert add(1, 3) == 4

    a, b = map(int, input(': ').split())
    print(f'result: {add(a, b)}')