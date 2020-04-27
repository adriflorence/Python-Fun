# Starting from the number 0, find the minimum number of operations required to reach a given positive target number. You can only use the following two operations:

# 1. Add 1
# 2. Double the number

def min_operations(target):
    counter = 0
    
    while target != 0:
        if target % 2 == 1:
            target = target - 1
        else:
            target = target // 2
        counter += 1
        
    return counter

def test_function(test_case):
    target = test_case[0]
    solution = test_case[1]
    output = min_operations(target)
    print(min_operations(target))
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

# Test Cases

target_1 = 18
solution_1 = 6
test_case_1 = [target_1, solution_1]
test_function(test_case_1)

target_2 = 69
solution_2 = 9
test_case_2 = [target_2, solution_2]
test_function(test_case_2)

target_3 = 0
solution_3 = 0
test_case_3 = [target_3, solution_3]
test_function(test_case_3)