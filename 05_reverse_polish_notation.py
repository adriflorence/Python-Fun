# Reverse Polish Notation
# the operators come after the operands.
# For example: `3 1 + 4 *` would be evaluated as `(3 + 1) * 4 = 16`

class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def evaluate_post_fix(input_list):
    stack = Stack()
    operators = ['*', '+', '-', '/']
    for char in input_list:
        if char in operators:
            # cast to string so can be concatenated            
            second = str(stack.pop())
            first = str(stack.pop())
            output = int(eval(first + char + second))
            stack.push(output)
        else:
            stack.push(int(char))
    
    return stack.pop()

# TESTS

test1 = ["3", "1", "+", "4", "*"]
test2 = ["4", "13", "5", "/", "+"]
test3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evaluate_post_fix(test3))
assert evaluate_post_fix(test1) == 16
assert evaluate_post_fix(test2) == 6
assert evaluate_post_fix(test3) == 12