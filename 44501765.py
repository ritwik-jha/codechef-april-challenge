# cook your dish here
# cook your dish here
import numpy as np
def worthy_matrix(A,N,M,K):
    count = 0
    smaller = min(N,M)
    final = []
    for i in range(1,smaller+1):
        final.append(all_sub(i,i,A))
    
    for variety in final:
        #print(variety)
        for matrix in variety:
            #print(matrix)
            avg = np.average(matrix)
            if avg >= K:
            #print(matrix)
            #print('-------------')
                count+=1
    #print(np.mat(final))
    return count            
        
    
def all_sub(r, c, mat): # returns all sub matrices of order r * c in mat
    arr_of_subs = []
    if (r == len(mat)) and (c == len(mat[0])):
            arr_of_subs.append(mat)
            return arr_of_subs
    for i in range(len(mat) - r + 1):
        for j in range(len(mat[0]) - c + 1):
            temp_mat = []
            for ki in range(i, r + i):
                temp_row = []
                for kj in range(j, c + j):
                    temp_row.append(mat[ki][kj])
                temp_mat.append(temp_row)
            arr_of_subs.append(temp_mat)
    return arr_of_subs

try:
    T = int(input())
    for i in range(T):
        N, M, K = list(map(int,input().split()))
        A = []
        for i in range(N):
            m = list(map(int,input().split()))
            A.append(m)
        print(worthy_matrix(A,N,M,K))
        
        
except:
    print('error')
