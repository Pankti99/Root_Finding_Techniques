

def func(x):
    return x ** 4 - x ** 3 - x ** 2 - 6 * x - 4


def false_position(a, b):

    d=(0.5 * 10 ** -4)
    z = 0

    if func(a) * func(b) >= 0:
        print("The initialization values are not correct")
        return -1

    print()
    print("------------------------------------------------------")
    print(end='  ')
    print(" a   |", end=' ')
    print(" f(a)  |", end='   ')
    print("b    |", end='  ')
    print("f(b)   |", end='  ')
    print("  c   | ", end='   ')
    print("f(c) ")
    print("------------------------------------------------------")

    c = a

    while ((c - z) < d):

        c1 = (a * func(b) - b * func(a)) / (func(b) - func(a))
        c=round(c1,6)

        if(z==c):
            break
        if (func(c) == 0.0):
            print(func(c))
            break

        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        z = c
        print("%.4f" % a, "|", "%.4f" % func(a), "|", "%.4f" % b, "|", "%.4f" % func(b), "|", "%.4f" % c, "|",
              "%.4f" % func(c))
        print()

    print("------------------------------------------------------")
    print("Value of root: ", "%.4f" % c)


a = -1
b = 2

false_position(a, b)
