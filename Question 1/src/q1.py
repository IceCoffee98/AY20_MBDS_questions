
# %%
'''
m:

'''
def get_route(m, n, q_sum):
    t_sum=q_sum
    step_list = []
    step_length=m+n-2

    t_sum -= m
    max_val = 0.5 * m * (m - 1) + (m - 1) * (n - 1)  # 能加上的最大值
    min_val = 0.5 * m * (m - 1) + 1 * (n - 1)  # 能加上的最小值

    while not(m == 1 and n == 1):
        if t_sum > max_val:  # 如果上方矩阵能提供的最大值小于剩下的sum，再本行还要再加一次
            t_sum -= m
            n -= 1
            step_list.append('R')
        else:
            t_sum -= m - 1
            m -= 1
            step_list.append('D')
        max_val = 0.5 * m * (m - 1) + (m - 1) * (n - 1)  # 能加上的最大值
        min_val = 0.5 * m * (m - 1) + 1 * (n - 1)  # 能加上的最小值

    # finally reverse the list to the right order
    reversed_step_list=list(reversed(step_list))

    return reversed_step_list

# %%
list1 = get_route(9, 9, 65)
print(65, '', end='')
for item in list1:
    print(item, end='')

# %%
list2 = get_route(9, 9, 72)
print(72, '', end='')
for item in list2:
    print(item, end='')

# %%
list3 = get_route(9, 9, 90)
print(90, '', end='')
for item in list3:
    print(item, end='')
# %%
list4 = get_route(9, 9, 100)
print(100, '', end='')
for item in list4:
    print(item, end='')
# %%
