# Given a sorted array that may have duplicate values, use *binary search* to find the **first** and **last** indexes of a given value.

# For example, if you have the array `[0, 1, 2, 2, 3, 3, 3, 4, 5, 6]` and the given value is `3`,
# the answer will be `[4, 6]` (because the value `3` occurs first at index `4` and last at index `6` in the array).

# The expected complexity of the problem is $O(log(n))$.

def first_and_last_index(arr, number):
    
    # find first occurence
    first = first_index(arr, number, 0, len(arr) - 1)
    
    # find last occurence
    last =  last_index(arr, number, 0, len(arr) - 1)
    return [first, last]

def first_index(arr, number, start, end):
    if start > end:
        return -1
    
    middle = start + (end - start) // 2
    if number == arr[middle]:
        # check if number appears earlier in the list
        current_start_position = first_index(arr, number, start, middle - 1)
        if current_start_position != -1:
            start_pos = current_start_position
        else:
            start_pos = middle
        return start_pos
    elif number < arr[middle]:
        return first_index(arr, number, start, middle - 1)
    else:
        return first_index(arr, number, middle + 1, end)


def last_index(arr, number, start, end):
    if start > end:
        return -1
    
    middle = start + (end - start) // 2
    if number == arr[middle]:
        # check if number appears later in the list
        current_end_position = last_index(arr, number, middle + 1, end)
        if current_end_position != -1:
            end_pos = current_end_position
        else: 
            end_pos = middle
        return end_pos
    elif number > arr[middle]:
        return last_index(arr, number, middle + 1, end)
    else:
        return last_index(arr, number, start, middle - 1)

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# TEST CASES

input_list_1 = [1]
number_1 = 1
solution_1 = [0, 0]
test_case_1 = [input_list_1, number_1, solution_1]
test_function(test_case_1)

input_list_2 = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number_2 = 3
solution_2 = [3, 6]
test_case_2 = [input_list_2, number_2, solution_2]
test_function(test_case_2)

input_list_3 = [0, 1, 2, 3, 4, 5]
number_3 = 5
solution_3 = [5, 5]
test_case_3 = [input_list_3, number_3, solution_3]
test_function(test_case_3)

input_list_4 = [0, 1, 2, 3, 4, 5]
number_4 = 5
solution_4 = [5, 5]
test_case_3 = [input_list_4, number_4, solution_4]
test_function(test_case_3)