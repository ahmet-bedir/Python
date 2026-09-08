import numpy as np

# array_list = np.array([1, 2, 3, 4, 5, True, False, 7.7])
# array_list += 1

# print(array_list)
# print(type(array_list))
# print(np.__version__)

###
# array0 = np.array(9)  # 0D - Scalar (sıfır boyutlu)
# print(array0)
# print(f"Kaç boyutlu? {array0.ndim}")

# array1 = np.array([23,45,43,26])  # 1D (tek boyutlu array)
# print(array1)
# print(f"Kaç boyutlu? {array1.ndim}")

# array2 = np.array([
#     [9,2,5],
#     [8,3,2]])  # 2D (iki boyutlu array)
# print(array2)
# print(f"Kaç boyutlu? {array2.ndim}")

# array3 = np.array([
#     [[9,2,5],[8,3,2]],
#     [[7,3,4],[2,5,3]],
#     [[3,6,9],[1,4,5]]
#     ])  # 3D (üç boyutlu array)
# print(array3)
# print(f"Kaç boyutlu? {array3.ndim}")

###########
# array_list = np.array([1, 3, 5, 7, 9], ndmin=3)
# print(array_list)

# array_list = np.arange(5, 16, 1)
# print(array_list)
# print(array_list[0])

# array_2d = np.array([
#     [4, 6, 8, 9],
#     [3, 1, 77, 87]
# ])
# print(array_2d[0,2])  # 8
# print(array_2d[:,0])  # [4 3]
# print(array_2d[array_2d>75])  # [77 87]

array_3d = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ],
    [
        [13,14,15],
        [16,17,18]
    ]
])
print(array_3d[0,0])  # [1 2 3]
print(array_3d[0,0,2])  # 3