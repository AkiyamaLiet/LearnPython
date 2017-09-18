def Perm(L, k, m):
    if k==m:
        print L
    else:
        for i in range(k, m+1):
            L[k], L[i] = L[i], L[k]
            Perm(L, k+1, m)
            L[k], L[i] = L[i], L[k]
    
    
if __name__ == '__main__':
    L = [1, 2, 3, 4, 5]
    Perm(L, 0, len(L)-1)