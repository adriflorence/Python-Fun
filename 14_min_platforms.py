# Given arrival and departure times of trains on a single day in a railway platform,
# find out the minimum number of platforms required so that no train has to wait for the other(s) to leave.

# You will be given arrival and departure times in the form of a list.
# Time hh:mm would be written as integer 
# e.g. 9:30 would be written as 930
# Similarly, 13:45 would be given as 1345

def min_platforms(arrival, departure):
    arrival.sort()
    departure.sort()
    trains = len(arrival)
    platforms = 1
    result = 1
    i = 1
    j = 0
    
    while i < trains and j < trains:
        
        if arrival[i] < departure[j]:
            platforms += 1
            i += 1
            
            if platforms > result:
                result = platforms
        else:
            platforms -= 1
            j += 1
            
    return result

def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]
    
    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# TEST

arrival_1 = [900,  940, 950,  1100, 1500, 1800]
departure_1 = [910, 1200, 1120, 1130, 1900, 2000]
test_case_1 = [arrival_1, departure_1, 3]

test_function(test_case_1)


arrival_2 = [200, 210, 300, 320, 350, 500]
departure_2 = [230, 340, 320, 430, 400, 520]
test_case_2 = [arrival_2, departure_2, 2]

test_function(test_case_2)