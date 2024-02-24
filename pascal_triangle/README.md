# Pascal's Triangle Generator

This Python project generates Pascal's triangle up to the nth row and provides a function to print the generated triangle.

## Overview

Pascal's triangle is a triangular array of binomial coefficients. Each number in the triangle is the sum of the two directly above it. The first and last numbers in each row are always 1.

This project provides a Python function to generate Pascal's triangle up to the nth row and another function to print the generated triangle in a readable format.

## Requirement

Python 3.x

## Usage

1. **Generating Pascal's Triangle:**
   
   To generate Pascal's triangle up to a specific row, call the `pascal_triangle` function with the desired row number as an argument. This function returns a list of lists representing the Pascal's triangle.

   Example:
   ```python
   from 0-pascal_triangle import pascal_triangle

   triangle = pascal_triangle(5)

1. Printing Pascal's Triangle:

After generating the triangle using the pascal_triangle function, you can print it using the print_triangle function.

Example:
```py
def print_triangle(triangle):
    """
    Print the Pascal's triangle.

    Args:
        triangle (list): The Pascal's triangle represented as a list of lists.
    """
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))

print_triangle(triangle)
