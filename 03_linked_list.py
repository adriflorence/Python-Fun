class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
      self.head = None
      
  def prepend(self, value):
      if self.head is None:
          self.head = Node(value)
          return
      
      new_head = Node(value)
      self.head.next = self.head
      self.head = new_head

  
  def append(self, value):
      # O(N) operation as we have to iterate through
      # the entire list to add a new tail
      if self.head is None:
          self.head = Node(value)
          return

      node = self.head
      while node.next:
          node = node.next

      node.next = Node(value)
      
  
  def search(self, value):
      """ Search the linked list for a node with the requested value and return the node. """
      if self.head is None:
        return None

      node = self.head
      while node:
        if node.value == value:
          return node
        node = node.next
  
  def remove(self, value):
      """ Remove first occurrence of value. """
      
      # TODO: Write function to remove here
      
      pass
  
  def pop(self):
      """ Return the first node's value and remove it from the list. """
      
      # TODO: Write function to pop here
      
      pass
  
  def insert(self, value, pos):
      """ Insert value at pos position in the list. If pos is larger than the
          length of the list, append to the end of the list. """
      
      # TODO: Write function to insert here
      
      pass
  
  def size(self):
      """ Return the size or length of the linked list. """
      
      
      # TODO: Write function to get size here
      
      pass
  
  def to_list(self):
      out = []
      node = self.head
      while node:
          out.append(node.value)
          node = node.next
      return out



## Implementation testing

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
    