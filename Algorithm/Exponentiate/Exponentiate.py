def Exponentiate(x, n):
    m = n
    power = 1
    while(m):
        while(not m%2):
            m /= 2
            x *= x
        m -= 1
        power *= x
    return power


if __name__ == '__main__':
    print Exponentiate(3, 5)