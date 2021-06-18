
import numpy as np


def polynomial_dot(f,g):
    return f[0]*g[0] +\
            (1/2)*(f[0]*g[1] + f[1]*g[0]) +\
            (1/3)*(f[0]*g[2] + f[1]*g[1] + f[2]*g[0]) +\
            (1/4)*(f[0]*g[3] + f[1]*g[2] + f[2]*g[1] + f[3]*g[0]) +\
            (1/5)*(f[1]*g[3] + f[2]*g[2] + f[3]*g[1]) +\
            (1/6)*(f[2]*g[3] + f[3]*g[2]) +\
            (1/7)*(f[3]*g[3])



def ortho_normalize(m):
    dim = m.shape[0]

    K = np.zeros([dim,dim])

    for i in range(dim):
        K[i] = m[i].copy()
        for j in range(i):
            projection = polynomial_dot(K[i],K[j])
            orthogonal = K[i] - projection * K[j]
            K[i] = orthogonal.copy()
        
         
        norm = polynomial_dot(K[i],K[i])**0.5
        if norm:
            normed = K[i]/norm
            K[i] = normed
    
    return K


#print(polynomial_dot([1,2,0,0],[3,4,0,0]))


I = np.diag([1]*4)
print('orthogonalizing->',I)
print(ortho_normalize(I))

print('\n\n')

# wont work as polynomial_dot only defined for max degree 3 
I = np.diag([1]*10)
print('orthogonalizing->',I)
print(ortho_normalize(I))

