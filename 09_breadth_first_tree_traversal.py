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
  q = Queue()
  visit_order = list()
  node = tree.get_root()
  # add root to queue
  q.enq(node)
  # while queue is not empty:
  while len(q) > 0:
    # dequeue and visit that node
    node = q.deq()
    visit_order.append(node)
    # add left child if exists
    if node.has_left_child():
      q.enq(node.get_left_child())
    # add right child if exists
    if node.has_right_child():
      q.enq(node.get_right_child())

  return visit_order


# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

print(breadth_first_search(tree))