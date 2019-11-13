import math

""" Node class
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

""" BST class with insert and display methods. display pretty prints the tree
"""

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            #create first node
            self.root = Node(data)                            
        else:
            #create leaf if the root is already created
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                #Recurse to the botom of the tree
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                #Recurse to the botom of the tree
                self._insert(data, cur_node.right)
        else:
            print("Value already present in tree")

    def find_i(self, target):
        cur_node = self.root
        if self.root is None :
            return None
        while cur_node:
            if cur_node.data == target:
                return True
            elif cur_node.data > target:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return False
            
    def find_r(self, target):
        if self.root:
            if self._find_r(target,self.root):
                return True
            return False
        else:
            return None
    
    def _find_r(self, target, cur_node):
        if target > cur_node.data and cur_node.right:
            return self._find_r(target, cur_node.right)
        elif target < cur_node.data and cur_node.left:
            return self._find_r(target, cur_node.left)
        if target == cur_node.data:
            return True
        if cur_node.left is None and cur_node.right is None and target != cur_node.data:
            return False

    def display(self, cur_node):
        if (self.root != None) :
            lines, _, _, _ = self._display(cur_node)
            for line in lines:
                print(line)
        else:
            print("No tree")

    def _display(self, cur_node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if cur_node.right is None:
            lines, n, p, x = self._display(cur_node.left)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if cur_node.left is None:
            lines, n, p, x = self._display(cur_node.right)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display(cur_node.left)
        right, m, q, y = self._display(cur_node.right)
        s = '%s' % cur_node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

bst = BinaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
bst.insert(8)
##bst.insert(9)
##bst.insert(10)
##bst.insert(11)
##bst.insert(12)
##bst.insert(13)
##bst.insert(14)
##bst.insert(15)
##bst.insert(100)
##bst.insert(200)

bst.display(bst.root)
