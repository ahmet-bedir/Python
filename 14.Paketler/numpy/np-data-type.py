import numpy as np

arr = np.array(1)
print(arr.dtype)  # int64 (=8byte) (varsayılan uzunluk)

arr = np.array(1, dtype=np.int8)
print(arr.dtype)  # int8 (=1byte) (uzunluğu kendimiz belirledik)

arr = np.array([1.22, 5.38, 8.41], dtype=np.float32)
print(arr.dtype)  # int8 (=1byte)

arr = np.array("ananaslar")
print(arr.dtype)  # <U9 (unicode)

# tür dönüşümü [float->int]
arr = np.array([4.32, 6.41, 8.4])
new_arr = arr.astype(int)
print(new_arr, new_arr.dtype)  # [4 6 8] int64

################
arr = np.array([111, 111111, 1111111111], dtype="i")
print(arr, arr.dtype)  # int32 (i ve i4 -> int32, i8 -> int64)

    