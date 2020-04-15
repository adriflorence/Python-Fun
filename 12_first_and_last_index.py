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
    pass


arr = [0, 1, 2, 2, 3, 3, 3, 4, 5, 6]
number = 3
print(first_and_last_index(arr, number))