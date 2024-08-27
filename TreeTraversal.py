# Tree Traversal task on leetcode 
# In progress

class Node:
  def __init__(self, val=None, children=None):
      self.val = val
      self.children = children 

ch1 = Node(val=3)
ch2 = Node(val=4)
ch3 = Node(val=5)

parent = Node(val=2, children=[ch1, ch2, ch3])

theRoot = Node(val=1, children=[parent])


  

def traverse(node, nodes): 
  if node is None:
    return 

  #print(node.val)

  if node.children: 
    for child in node.children: 
      traverse(child, nodes)

    #print(node.val)
    nodes.append(node.val)

  else: 
    nodes.append(node.val)
    
  return nodes

nodes = []
print(traverse(theRoot, nodes))

''' 

class Node:
  def __init__(self, val=None, children=None):
      self.val = val
      self.children = children 

def makeTree(order):
  if not order:
      return None

  root = Node(val=order[0])
  queue = [root]

  i = 2
  while i < len(order):
      currentNode = queue.pop(0)
      children = []

      while i < len(order) and order[i] is not None:
          childNode = Node(val=order[i])
          children.append(childNode)
          queue.append(childNode)
          i += 1

      currentNode.children = children

      i += 1

  return root

theRoot = makeTree(root)


  

def traverse(node, nodes): 
  if node is None:
    return 

  #print(node.val)

  if node.children: 
    for child in node.children: 
      traverse(child, nodes)

    #print(node.val)
    nodes.append(node.val)

  else: 
    nodes.append(node.val)
    
  return nodes

nodes = []
return traverse(theRoot, nodes)
'''
