# %%
# read the input file, save the coordinates in a coordinates_list as "x1'\t'x2"
# coordinates_list = ['16\t55', '27\t10',....., '24\t36', '33\t5']
with open('../input/input_coordinates_7_1.txt', 'r') as f:
    coordinates_list = f.read().split('\n')[1:-1]

# tranfer each of the item in coordinates_list as integer lists as x, y
# coordinates_points = [['16', '55'], ......, ['24', '36'], ['33', '5']]
coordinates_points = [point.split() for point in coordinates_list]

# string to int
# x1 = [16, 27, 48, 48, 5,...... 4, 33]
# x2 = [55, 10, 8, 2, 47,,...... 36, 5]
x1 = [int(p[0]) for p in coordinates_points]
x2 = [int(p[1]) for p in coordinates_points]

# %%
# calculate the index according to the equation and save them to the file
with open('../output/output_index_7_1.txt', 'w') as f:
    f.write('index\n')
    for i in range(len(x1)):
        index = x2[i] * 50 + x1[i]
        f.write(str(index) + '\n')

# %%
# read the input file, save the index in the index_list
# index_list = ['2283', '332',....., '942', '268']
with open('../input/input_index_7_1.txt', 'r') as f:
    index_list = f.read().split('\n')[1:-1]

# string to int
# index = [2283, 332, 1582,......, 619, 942, 268]
index = [int(p) for p in index_list]
print(index)

# %%
# calculate the coordinates according to the equation
# and save them to the file
with open('../output/output_coordinates_7_1.txt', 'w') as f:
    f.write('x1\tx2\n')
    for i in index:
        x2 = i // 50
        x1 = i - x2 * 50
        f.write(str(x1) + '\t' + str(x2) + '\n')

# # %%
# # test

# with open('../output/output_coordinates_7_1.txt', 'r') as f:
#     coordinates_list = f.read().split('\n')[1:-1]

# # tranfer each of the item in coordinates_list as integer lists as x, y
# # coordinates_points = [['16', '55'], ......, ['24', '36'], ['33', '5']]
# coordinates_points = [point.split() for point in coordinates_list]

# # string to int
# # x1 = [16, 27, 48, 48, 5,...... 4, 33]
# # x2 = [55, 10, 8, 2, 47,,...... 36, 5]
# x1 = [int(p[0]) for p in coordinates_points]
# x2 = [int(p[1]) for p in coordinates_points]

# with open('../output/output_reverse_7_1.txt', 'w') as f:
#     f.write('index\n')
#     for i in range(len(x1)):
#         index = x2[i] * 50 + x1[i]
#         f.write(str(index) + '\n')