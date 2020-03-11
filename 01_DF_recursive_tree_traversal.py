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

  
# visit node > traverse left subtree > traverse right subtree
def pre_order(tree):
  visit_order = list()
  root = tree.get_root()
  
  def traverse(node):
    if node:
      # visit node
      visit_order.append(node.get_value())
      # traverse left
      traverse(node.get_left_child())
      # traverse right
      traverse(node.get_right_child())

  traverse(root)
  return visit_order


# traverse left subtree > visit node > traverse right subtree
def in_order(tree):
  visit_order = list()
  root = tree.get_root()

  def traverse(node):
    if node:
      # traverse left
      traverse(node.get_left_child())
      # visit node
      visit_order.append(node.get_value())
      # traverse right
      traverse(node.get_right_child())

  traverse(root)
  return visit_order


# traverse left subtree > traverse right subtree > visit node
def post_order(tree):
  visit_order = list()
  root = tree.get_root()

  def traverse(node):
    if node:
      # traverse left
      traverse(node.get_left_child())
      # traverse right
      traverse(node.get_right_child())
      # visit node
      visit_order.append(node.get_value())

  traverse(root)
  return visit_order


# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

print(pre_order(tree))
# output: ['apple', 'banana', 'dates', 'cherry']

print(in_order(tree))
# output: ['dates', 'banana', 'apple', 'cherry']

print(post_order(tree))
# output: ['dates', 'banana', 'cherry', 'apple']