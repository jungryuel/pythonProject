def func(k):
    if k == 0:
        print('-' , end="")
        return

    func(k-1)
    print(' ' * 3 ** (k-1) ,end="")
    func(k-1)

while True:
    try:
        N = int(input())
        func(N)
        print()
    except:
        break