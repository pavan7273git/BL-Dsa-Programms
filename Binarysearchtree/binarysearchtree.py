class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Binarysearchtree:
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        if node is None:
            return TreeNode(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node


    def search(self, node, target):
        if node is None or node.data == target:
            return node
        if target < node.data:
            return self.search(node.left, target)
        else:
            return self.search(node.right, target)

    def inOrderTraversal(self, node):
        if node is not None:
            self.inOrderTraversal(node.left)
            print(node.data, end=" ")
            self.inOrderTraversal(node.right)


    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.minValueNode(node.right)
            node.data = temp.data
            node.right = self.delete(node.right, temp.data)
        return node

    def update(self, node, data, value):
        if self.search(node, data) is not None:
            node = self.delete(node, data)
            node = self.insert(node, value)
        return node