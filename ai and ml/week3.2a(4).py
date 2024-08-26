import numpy as np
import timeit
np.a=[4,5,1]
print(np.prod(np.a))
print("Time taken by vectorized product : ",end= "")
%timeit np.prod(np.a)
total = 1
for item in np.a:
total =total*item
t = total
print(t)
print("Time taken by iterative multiplication : ",end= "")
%timeit t
