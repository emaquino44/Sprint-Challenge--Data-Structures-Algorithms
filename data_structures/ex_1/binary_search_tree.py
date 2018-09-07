class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right= None

  def depth_first_for_each(self, cb):
    cb(self.value) #start at root
    if self.left:  #transverse left side
      self.left.depth_first_for_each(cb)  #mark that they have been visited
    if self.right: #then transverse the right side
      self.right.depth_first_for_each(cb)  #mark that they have been visited
    return

  def breadth_first_for_each(self, cb):
    nodes = [self ] #keep track of nodes
    while len(nodes) > 0:  #loop through checking nodes
      node = nodes.pop(0)  #pop first node from queue
      cb(node.value)
      if node.left:  # if checking on left, add to queue of nodes
        nodes.append(node.left)
      if node.right:  #if checking on right, add to queue of nodes
        nodes.append(node.right)


  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
