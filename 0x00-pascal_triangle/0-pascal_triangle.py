#!/usr/bin/python3
"""
A pascal triangle module
"""

def pascal_triangle(n):
    """
    Creates a Pascal's Triangle of size 'n'.

    Args:
        n: The size of the triangle (number of rows)

    Returns:
        A list of lists representing the triangle, or an empty list if n <= 0
    """

    if n <= 0:
        return []  

    triangle = [[1]]  # Initialize with the first row (always [1])
    for i in range(1, n):
        prev_row = triangle[i - 1]  
        current_row = [1]  # Each row starts with 1

        # Calculate the intermediate values
        for j in range(1, len(prev_row)):
            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)  # Each row ends with 1
        triangle.append(current_row)

    return triangle
