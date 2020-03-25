# Take a string as an input and return `True` if it's parentheses are balanced or `False` if it is not. 

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

def equation_checker(equation):
    # Intiate stack object
    stack = Stack()

    # Interate through equation checking parentheses
    for c in equation:
      if c == '(':
        stack.push(c)
      elif c == ')':
        if stack.pop() == None:
          return False
    
    # Return True if balanced and False if not
    if stack.size() == 0:
      return True
    else:
      return False

# TEST CASES
print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")