import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
import scipy.sparse as sp
import scipy.sparse.linalg as splinalg
import time

start = time.time()

blurryimg = loadmat('blurryimage.mat')['blurryimage']
B = blurryimg.flatten()

#print('IMG DATATYPE:',type(blurryimg))
# extend image by inserting a black boundary box
'''
hborder = np.array([[0]*64])
vborder = np.array([[0]*66])
img=np.concatenate((img,hborder),axis=0)
img=np.concatenate((hborder,img),axis=0)
img=np.concatenate((img,vborder.T),axis=1)
img=np.concatenate((vborder.T,img),axis=1)
'''
#print('IMG SHAPE:',blurryimg.shape)

plt.imshow(blurryimg,cmap='gray')
plt.savefig('blurryimage.png')

filters = []
for i in range(64):
    for j in range(64):
        z = np.zeros([64,64])
        
        # self weight
        z[i,j]=1/2

        # weights from vertical axis
        if (k:=i+1)<64:
            z[k,j]=1/8
        if (k:=i-1)>=0:
            z[k,j]=1/8


        # weights from horizontal axis
        if (k:=j+1)<64:
            z[i,k]=1/8
        if (k:=j-1)>=0:
            z[i,k]=1/8

        filters.append(z.flatten())


F = np.array(filters)

# check
'''
print('SHAPE F:',F.shape)
print(F[4*64+3][:(6*64)].reshape(6,64))
'''

import sys
method=sys.argv[1]

if method=='compare':
    method='naive|spinv|splu'

if 'naive' in method:
    
    #takes 9s to invert and get result
    I = np.linalg.inv(F) @ B
    Inaive = I.copy()

if 'spinv' in method:
    
    #convert to sparse
    FCSC = sp.csc_matrix(F)
    
    #takes 9s to invert as well, maybe saves memory when using sparse, but not compute
    I = splinalg.inv(FCSC).dot(B)
    Ispinv = I.copy()

if 'splu' in method:
    
    #convert to sparse
    FCSC = sp.csc_matrix(F)
    
    # https://stackoverflow.com/questions/15118177/inverting-large-sparse-matrices-with-scipy
    # takes 1s to do lu decomp
    lu_object = splinalg.splu(FCSC)

    #takes 6.5s
    # note result is transposed
    I = lu_object.solve(B) # recover original image I
    Isplu = I.copy()

# Note I was supposed to be a column vector but solve returns transpose, hence we have a row vector.
# We don't care so much as we have a vector, we need to care if we had given a matrix to solve instead of the vector B

end = time.time()

if method!='naive|spinv|splu':

    recoveredoriginalsharpimage = I.reshape(64,64)
    plt.imshow(recoveredoriginalsharpimage,cmap='gray')
    plt.savefig(f'recoveredoriginalsharpimage-{method}.png')
    #plt.show()
    
    print(f'METHOD:{method} | took -> {end - start} seconds...\n')

else:
    print(f'DIFF naive vs spinv ->',np.linalg.norm(Inaive - Ispinv))
    print(f'DIFF naive vs splu ->',np.linalg.norm(Inaive - Isplu))
    print(f'DIFF spinv vs splu ->',np.linalg.norm(Ispinv - Isplu))

