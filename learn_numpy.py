import numpy as np

print(np.iinfo(np.int64))

b = np.uint8(124)
print(b)
print(type(b))
print(np.iinfo(b))
print(np.iinfo(np.int8))

print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')

a = np.uint8(-456)
print(a)

arr = np.array([1,5,2,9,10], dtype = np.int8)
print(arr)

nd_arr = np.array([
               [12, 45, 78],
               [34, 56, 13],
               [12, 98, 76]
               ])

print(nd_arr)

print(arr.dtype)

arr2 = np.array([345234, 876362.12, 0, -1000, 99999999], dtype = np.float32)
print("")
print(arr2)
print("")
print("")

print(arr.ndim)
print(nd_arr.ndim)
print("")

print(arr.size)
print(nd_arr.size)
print("")

print(arr.shape)
print(nd_arr.shape)
print("")

print(arr.itemsize)
print(nd_arr.itemsize)
print("")

zeros_1d = np.zeros(5)
print(zeros_1d)
print("")

zeros_3d = np.zeros((5, 4, 3), dtype = np.float32)
print(zeros_3d)
print("")

arr3, step  = np.linspace(-6, 21, 60, retstep= True, endpoint= False)
print(step)

simplelist = [19, 242, 14, 152, 142, 1000]
overage= sum(simplelist)/len(simplelist)
print(overage)