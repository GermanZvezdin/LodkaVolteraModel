#
# Created by German Zvezdin on 13.02.2021.
#


E1 = 0.1
E2 = 1.2
MU = 0.6
E3 = MU * E1
h = 0.01
"""
def f1(y1, y2):
    return y1 * (E1 - y2)
def f2(y1, y2, y3):
    return y2 * (-E2 + y1 - y3)
def f3(y2, y3):
    return y3 * (-E3 + MU * y2)


def k1(func, x, y):
    return h * func(x, y)
def k1m(func, x, y, z):
    return h * func(x, y, z)

def k2(func,  x,  y,  k):
    return h * func(x + h/4, y + k/4)
def k2m(func,  x,  y,  z,  k):
    return h * func(x + h/4, y + k/4, z + k/4)

def k3(func, x, y, k1, k2):
    return h * func(x + 3 * h / 8, y + 3 * k1 / 32 + 9 * k2 / 32)
def k3m(func,  x,  y,  z,  k1,  k2):
    return h * func(x + 3 * h / 8, y + 3 * k1 / 32 + 9 * k2 / 32, z + 3 * k1 / 32 + 9 * k2 / 32)


def k4(func,  x,  y,  k1,  k2,  k3):
    return h * func(x + 12 * h / 13, y + 1932 * k1 / 2197 - 7200 * k2 / 2197 + 7296 * k3 / 2197)
def k4m(func,  x,  y,  z,  k1,  k2,  k3):
    return h * func(x + 12 * h / 13, y + 1932 * k1 / 2197 - 7200 * k2 / 2197 + 7296 * k3 / 2197,
                    z + 1932 * k1 / 2197 - 7200 * k2 / 2197 + 7296 * k3 / 2197)

def k5(func,  x,  y,  k1,  k2,  k3,  k4):
    return h * func(x + h, y + 439 * k1 / 216 - 8 * k2 + 3680 * k3 / 513 - 845 * k4 / 4104)
def k5m(func,  x,  y,  z,  k1,  k2,  k3,  k4):
    return h * func(x + h, y + 439 * k1 / 216 - 8 * k2 + 3680 * k3 / 513 - 845 * k4 / 4104,
                    z + 439 * k1 / 216 - 8 * k2 + 3680 * k3 / 513 - 845 * k4 / 4104)

def NexStepValue( y_prev,  k1,  k2,  k3,  k4,  k5):
    return y_prev + 25 * k1 / 216 + 1408 * k3 / 2565 + 2197 * k4 / 4101 - k5 / 5

"""



def f1(y1, y2):
    return y1 * (E1 - y2)
def f2(y1, y2, y3):
    return y2 * (-E2 + y1 - y3)
def f3(y2, y3):
    return y3 * (-E3 + MU * y2)


def k1(func, x, y):
    return func(x, y)
def k1m(func, x, y, z):
    return func(x, y, z)

def k2(func,  x,  y,  k):
    return func(x + h/2, y + k*h/2)
def k2m(func,  x,  y,  z,  k):
    return h * func(x + h/2, y + k/2, z + k*h/2)

def k3(func, x, y, k2):
    return func(x + h / 2, y + k2 * h / 2)
def k3m(func,  x,  y, z,  k2):
    return func(x + h / 2, y + k2 * h / 2, z + k2 * h / 2)


def k4(func,  x,  y, k3):
    return func(x + h, y + h * k3)
def k4m(func,  x,  y,  z, k3):
    return func(x + h, y + h * k3, z + h * k3)


def NexStepValue( y_prev,  k1,  k2,  k3,  k4):
    return y_prev + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6

if __name__ == "__main__" :

    y_1 = E2 - 1 + 0.25
    y_2 = E1 + 0.25
    y_3 = 1.0 + 0.25
    t = 0
    with open('f1.txt', 'w') as p1:
        with open('f2.txt', 'w') as p2:
            with open('f3.txt', 'w') as p3:
                with open('f12.txt', 'w') as p12:
                    with open('f13.txt', 'w') as p13:
                        with open('f23.txt', 'w') as p23:
                            while(t <= 100.0):

                                ck1 = k1(f1, y_1, y_2)
                                ck2 = k2(f1, y_1, y_2, ck1)
                                ck3 = k3(f1, y_1, y_2, ck2)
                                ck4 = k4(f1, y_1, y_2, ck3)


                                forY1 = [ck1, ck2, ck3, ck4]

                                ck1 = k1m(f2, y_1, y_2, y_3)
                                ck2 = k2m(f2, y_1, y_2, y_3, ck1)
                                ck3 = k3m(f2, y_1, y_2, y_3, ck2)
                                ck4 = k4m(f2, y_1, y_2, y_3, ck3)


                                forY2 = [ck1, ck2, ck3, ck4]

                                ck1 = k1(f3, y_2, y_3)
                                ck2 = k2(f3, y_2, y_3, ck1)
                                ck3 = k3(f3, y_2, y_3, ck2)
                                ck4 = k4(f3, y_2, y_3, ck3)


                                forY3 = [ck1, ck2, ck3, ck4]

                                y_1 = NexStepValue(y_1, forY1[0], forY1[1], forY1[2], forY1[3])

                                y_2 = NexStepValue(y_2, forY2[0], forY2[1], forY2[2], forY2[3])

                                y_3 = NexStepValue(y_3, forY3[0], forY3[1], forY3[2], forY3[3])

                                p1.write(f"{t} {y_1} \n")
                                p2.write(f"{t} {y_2} \n")
                                p3.write(f"{t} {y_3} \n")

                                p12.write(f"{y_1} {y_2} \n")
                                p13.write(f"{y_1} {y_3} \n")
                                p23.write(f"{y_2} {y_3} \n")
                                t += h
