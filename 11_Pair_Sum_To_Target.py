# Given an input_list and a target, return the indices of pair of integers in the list that sum to the target.
# The best solution takes O(n) time. You can assume that the list does not have any duplicates.

# For e.g. input_list = [1, 5, 9, 7] and target = 8, the answer would be [0, 3]

def pair_sum_to_zero(input_list, target):
  index_dictionary = dict()
  for index, element in enumerate(input_list):
    if target - element in index_dictionary:
      return [index_dictionary[target - element], index]
    index_dictionary[element] = index


test_case_1 = [[1, 5, 9, 7], 8]
test_case_2 = [[10, 5, 9, 8, 12, 1, 16, 6], 16]
test_case_3 = [[0, 1, 2, 3, -4], -4]

assert pair_sum_to_zero(test_case_1[0], test_case_1[1]), [0, 3]
assert pair_sum_to_zero(test_case_2[0], test_case_2[1]), [0, 7]
assert pair_sum_to_zero(test_case_3[0], test_case_3[1]), [0, 4]