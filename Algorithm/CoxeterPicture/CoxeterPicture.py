def CoxeterPicture(size):
    matrix = [[0 for i in range(size)] for i in range(size)]
    i = 0
    j = size / 2
    for key in range(1, size*size+1):
        matrix[i][j] = key
        #i -= 1
        #i %= size
        #j -= 1
        #j %= size
        k = i-1 if i else size-1
        l = j-1 if j else size-1
        if matrix[k][l]:
            i += 1
        else:
            i = k
            j = l
            
    for i in range(size):
        for j in range(size):
            print "%-2d" % matrix[i][j],
        print 
    
    

if __name__ == '__main__':
    CoxeterPicture(5)