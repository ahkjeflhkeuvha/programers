N = int(input())

class Node(object):
    def __init__(self, item):
        self.item = item
        self.right, self.left = None, None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def preorder(self):
        def _preorder(node):
            print(node.item, end="")
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)
        _preorder(self.root)

    def inorder(self):
        def _inorder(node):
            if node.left:
                _inorder(node.left)
            print(node.item, end="")
            if node.right:
                _inorder(node.right)
        _inorder(self.root)

    def postorder(self):
        def _postorder(node):
            if node.left:
                _postorder(node.left)
            if node.right:
                _postorder(node.right)
            print(node.item, end="")
        _postorder(self.root)


BT = BinaryTree()

for _ in range(N):
    root, left, right = input().split()
    if BT.root is None:
        BT.root = Node(root)
        if left != '.':
            BT.root.left = Node(left)
        if right != '.':
            BT.root.right = Node(right)
    else:
        nodes = [BT.root]
        while nodes:
            current = nodes.pop()
            if current.item == root:
                if left != '.':
                    current.left = Node(left)
                if right != '.':
                    current.right = Node(right)
                break
            if current.left:
                nodes.append(current.left)
            if current.right:
                nodes.append(current.right)

BT.preorder()
print()
BT.inorder()
print()
BT.postorder()
