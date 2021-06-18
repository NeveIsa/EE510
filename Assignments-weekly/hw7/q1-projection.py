import numpy as np


d=10
n=10

np.random.seed(1)
R = np.random.randn(d,n)
u = np.random.randn(d,1)


def projection(R,u,n):
    A = R[:n].T
    projMatrix = A @ np.linalg.pinv(A.T@A) @ A.T
    #print(projMatrix.shape)
    return projMatrix @ u


print(f'|u| -> {np.linalg.norm(u)}\n')


for n in range(1,11):
    proj = projection(R,u,n) 
    val = np.linalg.norm(u-proj)
    print(f'|u-projection(R,u,{n})| ->', val)


