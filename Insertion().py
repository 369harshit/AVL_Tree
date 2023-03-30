# Python code to insert a node in AVL tree

# Generic tree node class
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


# AVL tree class which supports the
# Insert operation
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

    # Recursive function to insert key in
    # subtree rooted with node and returns
    # new root of subtree.
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

    def preOrder(self, root):
        if not root:
            return
        print(root.val, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)


# Driver program to test above function
myTree = AVL_Tree()
root = None

root = myTree.insert(root, 10)
root = myTree.insert(root, 20)
root = myTree.insert(root, 30)
root = myTree.insert(root, 40)
root = myTree.insert(root, 50)
root = myTree.insert(root, 25)

# Preorder Traversal
print("Preorder traversal of the constructed AVL tree is")
myTree.preOrder(root)

