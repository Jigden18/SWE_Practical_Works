from collections import deque
# Step 1: Define the Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Step 2: Implement the Binary Search Tree Class
class BinarySearchTree:
    def __init__(self):
        self.root = None
    # Step 3: Implement the Insertion Method
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    # Step 4: Implement the Search Method
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
    # Step 5: Implement Traversal Methods
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    # Step 6: Implement the Deletion Method
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            node.value = self._min_value(node.right)
            node.right = self._delete_recursive(node.right, node.value)

        return node

    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

# Exercises for Students
# Implement a method to find the maximum value in the BST.
# Add a method to count the total number of nodes in the BST.
# Implement a level-order traversal (breadth-first search) for the BST.
# Create a method to find the height of the BST.
# Implement a method to check if the tree is a valid BST.
    
    # Step 7: Implement the Maximum Value Method
    def max_value(self):
        return self._max_value_recursive(self.root)

    def _max_value_recursive(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.value
    
    # Step 8: Implement the node count method
    def _count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)
    
    def count_nodes(self):
        return self._count_nodes_recursive(self.root)
    

    # Step 9: Implement the level-order traversal method
    def level_order_traversal(self):
        result = []
        if not self.root:
            return result

        queue = deque([self.root])  # Starting with the root in the queue
        while queue:
            node = queue.popleft()
            result.append(node.value)

            # Add the left and right children of the current node to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    # Step 10: Implement the height method
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1  # Base case: height of an empty tree
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)

    # Step 11: Implement the valid BST Check method
    def is_valid_bst(self):
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_valid_bst_recursive(self, node, min_val, max_val):
        if node is None:
            return True  # An empty tree is a valid BST

        # Check the current node's value
        if not (min_val < node.value < max_val):
            return False

        # Recursively check the left and right subtrees
        return (self._is_valid_bst_recursive(node.left, min_val, node.value) and
                self._is_valid_bst_recursive(node.right, node.value, max_val))


bst = BinarySearchTree()

# Insert nodes into the BST
values_to_insert = [15, 10, 20, 8, 12, 17, 25]
for value in values_to_insert:
    bst.insert(value)

# Test max_value method
print("Maximum value in the BST:", bst.max_value()) 

# Test count_nodes method
print("Total number of nodes:", bst.count_nodes())  

# Test level-order traversal
print("Level-order Traversal:", bst.level_order_traversal()) 

# Test height method
print("Height of the BST:", bst.height())  

# Test if the tree is a valid BST
print("tree is valid BST", bst.is_valid_bst())  