import numpy as n
import tensorflow as t
s=50
print("Scalar : ",s)
m=n.array([[0, 2],[2, 3]])
v=n.array([[0, 2]])
print("\nMatrix:\n",m)
print("\nVector:\n",v)
print("\nTensor:")
fill_2d = t.fill([3, 3],4, '2d')
fill_string = t.fill([2, 2], "str", 'fill_tensor_string')
print("\nNumerics:\n",fill_2d)
print("\nString:\n",fill_string)
g=n.gradient(m)
print("\nGradient:\n",g)
w,v = n.linalg.eig(m)
mat_norm = n.linalg.norm(m)
print("\nEigen values:\n",w)
print("\nEigen vectors:\n",v)
print("\nMatrix norm:",mat_norm)

