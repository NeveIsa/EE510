import time
import numpy as np
import scipy.sparse
import scipy.sparse.linalg

trials=10

def mul(n):
    print('mul')
    A = np.random.randn(n,n)
    B = np.random.randn(n,n)

    start=time.time()

    for i in range(trials):
        C = A@B

    end=time.time()
    average = (end - start)/trials
    print(n,'->',average*1000) #in ms




def inv(n): 
    print('inv')
    A = np.random.randn(n,n)
    b = np.random.randn(n)
     
    start=time.time()
    for i in range(trials):
        np.linalg.inv(A)*b

    end = time.time()
    average = (end - start)/trials
    print(n,'->',average*1000) #in ms


def invsparse(n):
    print('invsparse')

    i = np.random.randint(n)
    j = np.random.randint(n)
    
    A = scipy.sparse.lil_matrix((n,n))
    A[i,j] = np.random.randn() 
    
    # Add small value on diagonal to make non singular
    A += 0.00001*np.eye(n)
    
    #A = A.tocsr()
    A = A.tocsc()

    b = np.random.randn(n)
    

    start=time.time()
    for i in range(trials):
        scipy.sparse.linalg.inv(A)*b

    end = time.time()
    average = (end - start)/trials
    print(n,'->',average*1000) #in ms

#inv(1000)
#inv(2000)

invsparse(1000)
invsparse(2000)



