# creates Node class that will hold relevant data at each junction in the linked list
class Node:
  
  #constructor
  def __init__(self, description, value, vin):
    self.description = description
    self.value = value
    self.vin = vin
    self.next = None

  def __repr__(self):
    return self.value

# creates Linked List class
class LinkedList:
  # constructor
  def __init__(self, nodes=None):
    self.head = None
    if nodes is not None:
      node = Node(data=nodes.pop(0))
      self.head = node
      for elem in nodes:
        node.next = Node(data=elem)
        node = node.next  

  # allows us to print out the linked list and get a visual representation to visualize how it is functioning
  def __repr__(self):
    node = self.head
    nodes = []
    while node is not None:
      nodes.append(node.value)
      node = node.next
    nodes.append("None")
    return " -> ".join(nodes)

  # allows for iteration through the linked list (i.e. for node in llist)
  def __iter__(self):
    node = self.head
    while node is not None:
      yield node
      node = node.next

  # adds a new node to the front of the linked list
  def add_first(self, node):
    node.next = self.head
    self.head = node

  # removes a node based on the contents of the parameter 'target_node_data'
  def remove_node(self, target_node_data):
    if not self.head:
      raise Exception("List is empty")

    if self.head.data == target_node_data:
      self.head = self.head.next
      return

    previous_node = self.head
    for node in self:
      if node.data == target_node_data:
        previous_node.next = node.next
        return
      previous_node = node

    raise Exception("Node with data '%s' not found" % target_node_data)
