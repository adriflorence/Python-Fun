from collections import deque

# Define Node Class #
class Node(object):
        
  def __init__(self, value = None):
    self.value = value
    self.left = None
    self.right = None

  def get_value(self):
    return self.value
      
  def set_value(self, value):
    self.value = value

  def get_left_child(self):
    return self.left

  def set_left_child(self, left):
    self.left = left

  def get_right_child(self):
    return self.right

  def set_right_child(self, right):
    self.right = right

  def has_left_child(self):
    return self.left != None

  def has_right_child(self):
    return self.right != None


# Define Tree Class #
class Tree():
    def __init__(self, value = None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root

# Define Queue Class #
class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

def breadth_first_search(tree):
  # queue
  q = Queue()
  # visit_order
  visit_order = list()
  # start at root
  node = tree.get_root()
  # while queue is not empty:
    # dequeue the node

    # visit that node

    # add left child if exists

    # add right child if exists
  pass


# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

breadth_first_search(tree)