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

  

def pre_order(tree):
  visit_order = list()
  root = tree.get_root()
  
  def traverse(node):
    if node is not None:
      # visit node

      # traverse left

      # traverse right
      pass
  traverse(root)
  return visit_order



tree = Tree("apple")
print(pre_order(tree))