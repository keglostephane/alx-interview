#!/usr/bin/python3
"""pascal_triangle

This module provide ``pascal triangle`` that returns a list of integers,
representing the Pascal's triangle of n.
"""


def pascal_triangle(n):
    """"Returns a list of list of intgers representing the Pascal triangle
    of ``n``

    :param n: height of the triangle
    :type n: int
    """
    triangle = []
    for i in range(n):
        if not i:
            triangle.append([1])
        elif i == 1:
            triangle.append([1, 1])
        else:
            prev_list = triangle[-1]
            new_list = [1]
            new_list.extend([prev_list[i] + prev_list[i+1]
                             for i in range(len(prev_list) - 1)])
            new_list.append(1)
            triangle.append(new_list)

    return triangle
