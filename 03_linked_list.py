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
      
      tmp = self.head
        
      self.head = Node(value)
      self.head.next = tmp
      
      return

  
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
      if self.head is None:
        return

      if self.head.value == value:
          self.head = self.head.next
          return

      node = self.head
      while node.next:
          if node.next.value == value:
              node.next = node.next.next
              return
          node = node.next
  
  def pop(self):
      if self.head is None:
          return None

      node = self.head
      self.head = self.head.next

      return node.value
  
  def insert(self, value, pos):
      """ Insert value at pos position in the list. If pos is larger than the
          length of the list, append to the end of the list. """
      
      # TODO: Write function to insert here
      
      pass
  
  def size(self):
      size = 0
      node = self.head
      while node:
        size += 1
        node = node.next

      return size
  
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
assert linked_list.to_list() == [1]
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3]

# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1]
linked_list.append(3)
assert linked_list.to_list() == [1, 3]

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1
assert linked_list.search(4).value == 4

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3]
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3]
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4]

# Test pop
value = linked_list.pop()
assert value == 2
assert linked_list.head.value == 1