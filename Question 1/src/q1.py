
# %%


def get_route(m, n, q_sum):
    t_sum = q_sum
    step_list = []
    t_sum -= m
    max_val = 0.5 * m * (m - 1) + (m - 1) * (n - 1)  # 能加上的最大值
    while not (m == 1 and n == 1):
        if t_sum > max_val:  # 如果上方矩阵能提供的最大值小于剩下的sum，再本行还要再加一次
            t_sum -= m
            n -= 1
            step_list.append('R')
        else:
            t_sum -= m - 1
            m -= 1
            step_list.append('D')
        max_val = 0.5 * m * (m - 1) + (m - 1) * (n - 1)  # 能加上的最大值

    # finally reverse the list to the right order
    reversed_step_list = list(reversed(step_list))
    return reversed_step_list


# %%


def write_output(q_sum, list):
    output_file = open('../output/output', 'a')
    output_file.write(str(q_sum) + ' ' + ''.join(list) + '\n')
    output_file.close()


# %%
list1 = get_route(9, 9, 65)
print(65, ''.join(list1))
write_output(65, list1)

# %%
list2 = get_route(9, 9, 72)
print(72, ''.join(list2))
write_output(72, list2)

# %%
list3 = get_route(9, 9, 90)
print(90, ''.join(list3))
write_output(90, list3)

# %%
list4 = get_route(9, 9, 100)
print(100, ''.join(list4))
write_output(100, list4)

# %%
