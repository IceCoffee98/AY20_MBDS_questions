# %%
# %%
# read the input file, save the coordinates in a coordinates_list as "x1'\t'x2"
with open('../input/input_coordinates_7_2.txt', 'r') as f:
    coordinates_list = f.read().split('\n')[1:-1]

# tranfer each of the item in coordinates_list as integer lists as x, y
coordinates_points = [point.split() for point in coordinates_list]

# string to int
x1 = [int(p[0]) for p in coordinates_points]
x2 = [int(p[1]) for p in coordinates_points]
x3 = [int(p[2]) for p in coordinates_points]
x4 = [int(p[3]) for p in coordinates_points]
x5 = [int(p[4]) for p in coordinates_points]
x6 = [int(p[5]) for p in coordinates_points]

# %%
# calculate the index according to the equation and save them to the file
A2 = 4
A3 = 4 * 8
A4 = 4 * 8 * 5
A5 = 4 * 8 * 5 * 9
A6 = 4 * 8 * 5 * 9 * 6
with open('../output/output_index_7_2.txt', 'w') as f:
    f.write('index\n')
    for i in range(len(x1)):
        index = x1[i] + x2[i] * A2 + x3[i] * A3 + \
            x4[i] * A4 + x5[i] * A5 + x6[i] * A6
        f.write(str(index) + '\n')

# %%
# read the input file, save the index in the index_list
with open('../input/input_index_7_2.txt', 'r') as f:
    index_list = f.read().split('\n')[1:-1]

# string to int
index = [int(p) for p in index_list]
print(index[0:10])

# %%
# calculate the coordinates according to the equation
# and save them to the file
with open('../output/output_coordinates_7_2.txt', 'w') as f:
    f.write('x1\tx2\tx3\tx4\tx5\tx6\n')
    for i in index:
        x6 = i // A6
        x5 = (i - A6 * x6) // A5
        x4 = (i - A6 * x6 - A5 * x5) // A4
        x3 = (i - A6 * x6 - A5 * x5 - A4 * x4) // A3
        x2 = (i - A6 * x6 - A5 * x5 - A4 * x4 - A3 * x3) // A2
        x1 = i - A6 * x6 - A5 * x5 - A4 * x4 - A3 * x3 - A2 * x2
        f.write(
            str(x1) + '\t' + str(x2) + '\t' + str(x3) + '\t' + str(x4) + '\t' +
            str(x5) + '\t' + str(x6) + '\n')

# # %%
# # test
# # read the input file, save the coordinates in a coordinates_list as "x1'\t'x2"
# with open('../output/output_coordinates_7_2.txt', 'r') as f:
#     coordinates_list = f.read().split('\n')[1:-1]

# # tranfer each of the item in coordinates_list as integer lists as x, y
# coordinates_points = [point.split() for point in coordinates_list]

# # string to int
# x1 = [int(p[0]) for p in coordinates_points]
# x2 = [int(p[1]) for p in coordinates_points]
# x3 = [int(p[2]) for p in coordinates_points]
# x4 = [int(p[3]) for p in coordinates_points]
# x5 = [int(p[4]) for p in coordinates_points]
# x6 = [int(p[5]) for p in coordinates_points]

# print(x1[0], x2[0], x3[0], x4[0], x5[0], x6[0])
# print(len(x1))
# print(len(x2))

# # calculate the index according to the equation and save them to the file
# A2 = 4
# A3 = 4 * 8
# A4 = 4 * 8 * 5
# A5 = 4 * 8 * 5 * 9
# A6 = 4 * 8 * 5 * 9 * 6
# with open('../output/output_reverse_index_7_2.txt', 'w') as f:
#     f.write('index\n')
#     for i in range(len(x1)):
#         index = x1[i] + x2[i] * A2 + x3[i] * A3 + \
#                     x4[i] * A4 + x5[i] * A5 + x6[i] * A6
#         f.write(str(index) + '\n')

# %%
