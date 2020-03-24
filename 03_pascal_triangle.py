# Find and return the nth row of Pascal's triangle in the form a list
# For exmaple, if `n = 4`, then `output = [1, 4, 6, 4, 1]`.
# To know more about Pascal's triangle: https://www.mathsisfun.com/pascals-triangle.html
import math

def combination(n, r):
  return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))


def nth_row_pascal(n):
  result = []

  for line in range(n + 1):
    row = []
    for element in range(line + 1):
      row.append(combination(line, element))
    result.append(row)

  return result[n]


# tests
assert nth_row_pascal(0), [1]
assert nth_row_pascal(1), [1, 1]
assert nth_row_pascal(2), [1, 2, 1]
assert nth_row_pascal(3), [1, 3, 3, 1]
assert nth_row_pascal(4), [1, 4, 6, 4, 1]