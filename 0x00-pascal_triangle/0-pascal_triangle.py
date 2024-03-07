#!/usr/bin/python3
def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) != n:
        prev = triangle[-1]
        new = [1]
        for i in range(len(prev) - 1):
            new.append(prev[i] + prev[i + 1])
        new.append(1)
        triangle.append(new)
    return triangle
