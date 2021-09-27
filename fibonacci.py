def fib(num):
    p, q = 0, 1
    while(p<num):
        yield p
        p, q = q, p+q

for i in fib(100):
    print(i)