# %%
import matplotlib.pyplot as plt

# %%
with open('../input/input_question_6_polygon', 'r') as f:
    polys = f.read().split('\n')[:-1]

poly_points = [point.split() for point in polys]

x = [int(p[0]) for p in poly_points]
y = [int(p[1]) for p in poly_points]
plt.figure()
plt.scatter(x, y)

for i in range(len(x) - 1):
    plt.plot((x[i], x[i + 1]), (y[i], y[i + 1]))
plt.plot((x[0], x[-1]), (y[0], y[-1]))
for i_x, i_y in zip(x, y):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))

plt.show()

# %%
with open('../input/input_question_6_points', 'r') as f:
    content = f.read().split('\n')[:-2]

points = [point.split() for point in content]

x_p = [int(p[0]) for p in points]
y_p = [int(p[1]) for p in points]
plt.figure()
plt.scatter(x, y)

for i in range(len(x) - 1):
    plt.plot((x[i], x[i + 1]), (y[i], y[i + 1]))

plt.plot((x[0], x[-1]), (y[0], y[-1]))
for i_x, i_y in zip(x, y):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))

plt.scatter(x_p, y_p)
for i_x, i_y in zip(x_p, y_p):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.show()

poly_points = [[int(p) for p in point] for point in poly_points]
points = [[int(p) for p in point] for point in points]


# %%
def is_in_poly(p, poly):

    px, py = p
    is_in = 'outside'
    for i, corner in enumerate(poly):
        next_i = i + 1 if i + 1 < len(poly) else 0
        x1, y1 = corner
        x2, y2 = poly[next_i]
        if (x1 == px and y1 == py) or (x2 == px
                                       and y2 == py):  # if point is on vertex
            is_in = 'inside'
            break
        if min(y1, y2) < py <= max(y1, y2):  # find horizontal edges of polygon
            x = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if x == px:  # if point is on edge
                is_in = 'inside'
                break
            elif x > px:  # if point is on left-side of line
                if is_in == 'inside':
                    is_in = 'outside'
                else:
                    is_in = 'inside'
                # is_in = not is_in
    return is_in


# %%
with open('../output/output_question_6', 'w') as f:
    for point in points:
        res = is_in_poly(point, poly_points)
        f.write(str(point[0]) + '\t' + str(point[1]) + '\t' + res + '\n')
        print(point, res)
# %%
