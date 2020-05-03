# The task is to find the length of the Longest Palindromic Subsequence (LPS)
# given a string of characters. 

def lps(input_string): 
    # create matrix for lookup table
    lookup_table = [[0 for x in range(len(input_string) + 1)] for x in range(len(input_string) + 1)]

    # The function should return one value: the LPS length for the given input string
    pass

def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

# TEST

string_1 = "TACOCAT"
solution_1 = 7
test_case_1 = [string_1, solution_1]
test_function(test_case_1)

string_2 = "BANANA"
solution_2 = 5
test_case_2 = [string_2, solution_2]
test_function(test_case_2)