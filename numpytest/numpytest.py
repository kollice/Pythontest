import numpy as np
import time

# def sum():
#     start = time.time()
#     X = np.arange(100000)
#     Y = np.arange(100000)
#     Z = X + Y
#     end = time.time()
#     print("result:",Z)
#     return end -start
# print(' time sum numpy:',sum())

## 生成数组以及随机生成数组元素示例
# a = np.array([1,2,3,4,5],float)
# print(a)
# print(type(a))
# print(a.tolist())
# print(list(a))
# b = a.copy()
# b.fill(1)
# print(b)
# print(np.random.permutation(4))
# print(np.random.normal(0,1,5))
# print(np.random.random(6))
#
# print(np.identity(5, dtype=float))
# print(np.eye(5, k=1, dtype=int))
# print(np.eye(5, k=2, dtype=int))
# print(np.eye(5, k=3, dtype=int))
# print(np.ones([2,3],dtype=int))
# print(np.zeros([3,5], dtype=int))
# d = np.array([[1,2,3],[4,5,6]],float)
# print(d)
# print(np.ones_like(d, dtype=int))
# print(np.zeros_like(d,dtype=int))
# d1 = np.ones_like(d, dtype=int)
# d2 = np.zeros_like(d,dtype=int)
# d3 = np.vstack([d1,d2])
# print(d3)
# print(np.random.rand(5))
# print(np.random.multivariate_normal([0, 1], [[2, 3], [3, 4]], size=[5, ]))


# arr = np.array([2., 6., 5., 5.])
# print(np.unique(arr))
# print(np.sort(arr))
# print(np.argsort(arr))
# np.random.shuffle(arr)
# print(arr)
# cop = arr.copy()
# print(np.array_equal(cop, arr))
# print(np.array_equal(arr, np.array([2, 6, 5, 5])))

# matrix = np.array([[10, 29, 23], [24, 25, 46]], float)
# print(matrix)
# print(matrix.flatten())
# print(matrix.shape,matrix.dtype)
# newmatrix = matrix.astype(np.int32)
# print(newmatrix.dtype)
# print(np.alen(matrix))
# print(len(matrix))
# print(29 in matrix)

arr = np.array(range(35), dtype=float)
print(arr)
other = arr.reshape([7, 5])
print(other)
print(np.transpose(other))
