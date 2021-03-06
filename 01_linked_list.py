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
      # Search the linked list for a node with the requested value and return the node
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
      #  Return the first node's value and remove it from the list.
      if self.head is None:
          return None

      node = self.head
      self.head = self.head.next

      return node.value
  
  def insert(self, value, pos):
      # Insert value at pos position in the list. If pos is larger than the
      # length of the list, append to the end of the list
      if pos == 0:
        self.prepend(value)
        return

      index = 0
      node = self.head
      while node.next and index <= pos:
        if(pos-1) == index:
          new_node = Node(value)
          new_node.next = node.next
          node.next = new_node
          return

        index += 1
        node = node.next
      else: self.append(value)
  
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

  def __iter__(self):
    node = self.head
    while node:
        yield node.value
        node = node.next


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

# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4]
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4]
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3]

# Test size
assert linked_list.size() == 5


# REVERSE #

# NOT method of LinkedList Class !!
# Time complexity O(N)
def reverse(linked_list):
  new_list = LinkedList()
  node = linked_list.head
  prev_node = None

  for value in linked_list:
    new_node = Node(value)
    new_node.next = prev_node
    prev_node = new_node
  new_list.head = prev_node
  return new_list

# Test reverse
llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

flipped = reverse(llist)
is_correct = list(flipped) == list([0,-3,1,5,2,4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")