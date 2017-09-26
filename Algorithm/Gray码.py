def Gray(L, n):
    if n==1:
        L[0] = 0
        L[1] = 1
    else:
        Gray(L, n-1)
        for i in range(0, 2**(n-1)):
            L[2**n-i-1] = L[i] + 2**(n-1)
    

if __name__ == '__main__':
    L = [0]*(2**4)
    Gray(L, 1)
    print L