import sys

# initial value
x=[0,0,0,0]

#iteration in loop
for i in range(3):
    x[0]=(1./12)*(29-2*x[1]-3*x[2]+x[3])
    x[1]=(1./8)*(5+x[0]+2*x[2]-x[3])
    x[2]=(1./10)*(42-2*x[0]-3*x[1]+x[3])
    x[3]=(1./6)*(-24-x[0]-x[1]+x[2])

#iteration
'''
x[0]=(1./12)*(29-2*x[1]-3*x[2]+x[3])
x[1]=(1./8)*(5+x[0]+2*x[2]-x[3])
x[2]=(1./10)*(42-2*x[0]-3*x[1]+x[3])
x[3]=(1./6)*(-24-x[0]-x[1]+x[2])
'''

# making list of x

# print x
print(x)


################################################################

# the method from Inet 1


import numpy as np

ITERATION_LIMIT = 2

# initialize the matrix
A = np.array([[12., 2., 3., -1.],
              [-1., 8., -2., 1.],
              [2., 3., 10., -1.],
              [1., 1., -1., 6.]])
# initialize the RHS vector
b = np.array([29., 5., 42., -24.])

# prints the system
print("System:")
for i in range(A.shape[0]):
    row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    print(" + ".join(row), "=", b[i])
print()

x = np.zeros_like(b)
for it_count in range(ITERATION_LIMIT):
    print("Current solution:", x)
    x_new = np.zeros_like(x)

    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x_new[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]

    if np.allclose(x, x_new, rtol=1e-8):
        break

    x = x_new

print("Solution:")
print(x)
error = np.dot(A, x) - b
print("Error:")
print(error)

################################################################
#2dn methon from inet




import numpy as np
from scipy.linalg import solve

def gauss(A, b, x, n):

    L = np.tril(A)
    U = A - L
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        print str(i).zfill(3),
        print(x)
    return x

'''___MAIN___'''


A = np.array([[12., 2., 3., -1.],
              [-1., 8., -2., 1.],
              [2., 3., 10., -1.],
              [1., 1., -1., 6.]])
b = np.array([29., 5., 42., -24.])
#A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
#b = [1.0, 2.0, 3.0]
x = [0, 0, 0, 0]

n = 3

print gauss(A, b, x, n)
print solve(A, b)
