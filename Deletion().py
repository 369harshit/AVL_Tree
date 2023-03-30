# Python code to delete a node in AVL tree
# Generic tree node class
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


# AVL tree class which supports insertion,
# deletion operations
def getHeight(root):
    if not root:
        return 0
    return root.height


def getBalance(root):
    if not root:
        return 0
    return getHeight(root.left) - getHeight(root.right)


def rightRotate(z):
    y = z.left
    T3 = y.right

    # Perform rotation
    y.right = z
    z.left = T3

    # Update heights
    z.height = 1 + max(getHeight(z.left), getHeight(z.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))

    # Return the new root
    return y


def leftRotate(z):
    y = z.right
    T2 = y.left

    # Perform rotation
    y.left = z
    z.right = T2

    # Update heights
    z.height = 1 + max(getHeight(z.left), getHeight(z.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))

    # Return the new root
    return y


class AVL_Tree:

    def insert(self, root, key):

        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(getHeight(root.left), getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = leftRotate(root.left)
            return rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = rightRotate(root.right)
            return leftRotate(root)
        return root

    # Recursive function to delete a node with
    # given key from subtree with given root.
    # It returns root of the modified subtree.
    def delete(self, root, key):

        # Step 1 - Perform standard BST delete
        if not root:
            return root

        elif key < root.val:
            root.left = self.delete(root.left, key)

        elif key > root.val:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        # If the tree has only one node,
        # simply return it
        if root is None:
            return root

        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(getHeight(root.left), getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and getBalance(root.left) >= 0:
            return rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and getBalance(root.right) <= 0:
            return leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and getBalance(root.left) < 0:
            root.left = leftRotate(root.left)
            return rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and getBalance(root.right) > 0:
            root.right = rightRotate(root.right)
            return leftRotate(root)
        return root

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def preOrder(self, root):

        if not root:
            return
        print(root.val, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)


myTree = AVL_Tree()
root = None
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for num in nums:
    root = myTree.insert(root, num)

# Preorder Traversal
print("Preorder Traversal after insertion -")
myTree.preOrder(root)


# Delete
key = 10
root = myTree.delete(root, key)

# Preorder Traversal
print("\nPreorder Traversal after deletion -")
myTree.preOrder(root)
