#%%
L = 5
R = 12
B = 13
print('R:', R)
print('B:', B)

#%%
matrixs = []

for row in range(L):
    if row % 2 == 0:
        matrixs.append(['B', 'R', 'B', 'R', 'B'])
        R -= 2
        B -= 3
    else:
        matrixs.append(['R', 'B', 'R', 'B', 'R'])
        R -= 3
        B -= 2
print('R:', R)
print('B:', B)
with open('../output/output_question_5_l=5', 'w') as f:
    for row in matrixs:
        for p in row:
            f.write(p + '\t')
        f.write('\n')

#%%
L = 64
R = 139
B = 1451
G = 977
W = 1072
Y = 457
print('R + B + Y:', R + B + Y)
print('G + W:', G + W)

#%%
matrixs = []

for row in range(L):
    cols = []
    if row % 2 == 0:
        for ind in range(32):
            if G != 0:
                cols.append('G')
                G -= 1
            else:
                cols.append('W')
                W -= 1

            if R != 0:
                cols.append('R')
                R -= 1
            elif B != 0:
                cols.append('B')
                B -= 1
            elif Y != 0:
                cols.append('Y')
                Y -= 1
            else:
                cols.append('U')

    else:
        for ind in range(32):
            if R != 0:
                cols.append('R')
                R -= 1
            elif B != 0:
                cols.append('B')
                B -= 1
            elif Y != 0:
                cols.append('Y')
                Y -= 1
            else:
                cols.append('U')

            if G != 0:
                cols.append('G')
                G -= 1
            else:
                cols.append('W')
                W -= 1
    matrixs.append(cols)

matrixs[63][62] = matrixs[0][0]
matrixs[0][0] = 'W'
W -= 1
print('R:', R)
print('B:', B)
print('Y:', Y)
print('G:', G)
print('W:', W)

with open('../output/output_question_5_l=64', 'w') as f:
    for row in matrixs:
        for p in row:
            f.write(p + '\t')
        f.write('\n')