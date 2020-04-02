import math
def func(x):
    return math.exp(x) - 3 * x - math.sin(x)

def derivFunc(x):
    return math.exp(x) - 3 -math.cos(x)

def newtonRaphson(x):
    cnt = 0
    z = 0

    print("----------------------------------------------------------------------------------------------------------")
    print("N   ", "\t Xn ", "\t  f(Xn)  ", "\t  f'(Xn)    ", "\t f(Xn)/f'(Xn)\t", "\tXn-f(Xn)/f'(Xn)")
    print("----------------------------------------------------------------------------------------------------------")
    print()
    h = func(x) / derivFunc(x)

    while abs(h) >= 0.0001:
        if cnt == 0:
            h = func(x) / derivFunc(x)
            x = x - h
            print(cnt, "\t|", "%.6f" % x0, "\t|", "%.6f" % func(x), "\t|", "%.6f" % derivFunc(x), "\t|", "%.6f" % h,
                  "\t|", "%.6f" % x)
            print()
        z = x
        cnt = cnt + 1
        h = func(x) / derivFunc(x)
        x = z - h
        if (cnt != 0):
            print(cnt, "\t|", "%.6f" % z, "\t|", "%.6f" % func(x), "\t|", "%.6f" % derivFunc(x), "\t|", "%.6f" % h,
                  "\t|", "%.6f" % x)
            print()

    print("-----------------------------------------------------------------------------------------------------")
    print()
    print("-----------------------------------------------------------------------------------------------------")
    print("The value of the root is : ", "%.4f" % x)


x0 = 0
newtonRaphson(x0)
