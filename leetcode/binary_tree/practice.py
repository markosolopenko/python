class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.right.right = Node(5)
tree.root.left.right = Node(6)
tree.root.right.left = Node(12)
print(f'     {tree.root.data} ')
print('   / ' + '   \\')
print(f'  {tree.root.left.data}      {tree.root.right.data}')
print(' / ' + '\\' + '    / ' + '\\')
print(f'{tree.root.left.left.data}   {tree.root.left.right.data}  '
      f'{tree.root.right.right.data}  {tree.root.right.left.data}')


