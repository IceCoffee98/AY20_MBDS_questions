# %%
''' Get the route from the top left corner to the bottom right corner as a list

The idea of a function is to go from the bottom right corner
to the top right corner. The option is either 'up' or 'right'.
Save each of the step in a list, and finally reverse the list as a return. 
For each of the step, say the current point is (i, j), consider
the matrix above: (i-1)*j. If the maximum number that this matrix can 
provide is smaller than the remaining part of sum, goes right, otherwise, 
goes up until it arrives the point of (1, 1). This is because the value
in the same line could provide a relative lager figure to be minus by the 
remaning part of sum.

Args:
    m: total lines of the matrix
    n: total columns of the matrix
    q_sum: sum that needs to be added

Return:
    the list of route that records the direction for each step. For example:

    ['D', 'R', 'R', 'R', 'D', 'D', 'D']

'''


def get_route(m, n, q_sum):
    # create a list to store the operation
    # the 'up' operation in the reversed direction corresponds to 
    # the 'down' operation in the original direction
    # the 'left' operation in the reversed direction corresponds to 
    # the 'right' operation in the original direction
    step_list = []

    # from the bottom right corner to the top right corner, the bottom right corner
    # is the first and must-pass point, so q_sum should minus this point first.
    q_sum -= m

    # calculate the maximum the matrix above can provide
    max_val = 0.5 * m * (m - 1) + (m - 1) * (n - 1)
    while not (m == 1 and n == 1):
        # If the maximum number that this matrix can 
        # provide is smaller than the remaining part of sum, goes left
        # otherwise, goes up. 
        if q_sum > max_val: 
            q_sum -= m
            n -= 1
            step_list.append('R')
        else:
            q_sum -= m - 1
            m -= 1
            step_list.append('D')
        
        # after moving forward, recalculate the maximum the matrix above can provide
        # because the matrix above is changed
        max_val = 0.5 * m * (m - 1) + (m - 1) * (n - 1) 

    # finally reverse the list to the right order and return
    reversed_step_list = list(reversed(step_list))
    return reversed_step_list


# %%
'''Write the outputs into the file

Args:
    q_sum: sum that needs to be added
    list: the list of operation

'''


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
# The number is too large. Sorry, I haven't find a solution yet
# list5 = get_route(90000, 100000, 87127231192)
# print(87127231192, ''.join(list5))
# %%
