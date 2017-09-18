import random

def Prime0(n):
    q = n-1
    large = 20
    for i in range(0, large):
        m = q
        a = random.randint(0,q-1) + 1
        y = 1
        z = a
        while m > 0:
            while (m % 2 == 0):
                z = (z * z) % n
                m /= 2
            m -= 1
            y = (y * z) % n
            #print a, y
        if  y != 1:
            return 0
    return 1


if __name__ == '__main__':
    for i in range(2,50):
        print i, " ", Prime0(i)