import numpy as np
import matplotlib.pyplot as plt
import sys

# constants
f_0,f_pi = int(sys.argv[1]),int(sys.argv[2]) # boundary conditions


L = np.pi # interval length
n = 1000   # discretization



# derived constants
a = n/L

def get_difference_eq_coeffs(k):
    # k = discrete step index

    # coeff y(k-1), y(k) , y(k-1)
    return a*a - 2*a, -2*a*a + 2*a, a*a



A = np.zeros((n+1,n+1))

A[0,0] = 1
A[-1,-1] =1

print(f'\nA->\n',A)

for k in range(1,n):
    row = np.zeros(n+1)
    row[k-1:k+2] = get_difference_eq_coeffs(k)
    A[k,:] = row


#print(A.shape)



xlinspace = np.linspace(L/n,L,n) # size = 100
temp = np.cos(xlinspace)

#temp[-1] with boundary conditions f_pi
temp[-1] = f_pi

# prepend b by f_0
b = np.zeros(n+1)
b[0]=f_0
b[1:]= temp



print(f'\nb->\n',b)
#print(b.size)

#solve for the y values in Ay = b
y = np.linalg.inv(A) @ b

print(f'\ny->\n',y)


plt.plot(np.linspace(0,L,n+1),y)
plt.savefig(f'{f_0} - {f_pi}.png')

