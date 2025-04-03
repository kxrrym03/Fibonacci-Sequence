def fib(n):
    a = 0
    b = 1

    print(a)
    if n > 1:
        print(b)

        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)

fib(5)