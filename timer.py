import timeit
for i in range(10):
    time = timeit.Timer("x.append(%d)" % i, "from __main__ import x")
    x= list(range(100000))
    t_opr = time.timeit(number=1000)
    print(t_opr)