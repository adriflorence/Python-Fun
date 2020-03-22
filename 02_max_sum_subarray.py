# You have been given an array containg numbers
# Find and return the largest sum in a contiguous subarray within the input array.

def max_sum_subarray(arr):
  max_sum = arr[0]
  current_sum = arr[0]

  for num in arr[1:]:
    current_sum = max(current_sum + num, num)
    max_sum = max(current_sum, max_sum)
  return max_sum

test_array_1 = [1, 2, 3, -4, 6]
test_array_2 = [1, 2, -5, -4, 1, 6]
test_array_3 = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
assert max_sum_subarray(test_array_1), 8   # sum of array
assert max_sum_subarray(test_array_2), 7   # sum of last two elements
assert max_sum_subarray(test_array_3), 18  # sum of subarray = [15, -13, 14, -1, 2, 1]