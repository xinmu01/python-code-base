class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    This is BST class. The values in left tree are smaller than root value,
    the values in right tree are equal or larger than root value.   
    """
    def __init__(self,rootValue):
        self.root = BinaryTreeNode(rootValue)

    def treeHeight(self):
        if not self.root:
            return 0
        leftHeight = self.treeHeight(self.root.left)
        rightHeight = self.treeHeight(self.root.right)
        return max(leftHeight,rightHeight) + 1
     
    def insertNode(self,value):
        self.root = self.insert_helper(self.root, value)
    
    def insert_helper(self, root, value):
        if root == None:
            return BinaryTreeNode(value)

        if value >= self.root.val:
            root.right = self.insert_helper(root.right,value)
        else:
            root.left = self.insert_helper(root.left, value)
        
        return root 

    def searchNode(self,value):
        return self.searchNodeHelper(self.root,value)

    def searchNodeHelper(self,root,value):
        if root == None:
            return False
        if value == root.val:
            return True
        elif value > root.val:
            return self.searchNodeHelper(root.right,value)
        else:
            return self.searchNodeHelper(root.left,value)

    def changeNode(self,value):
        pass

    def deleteNode(self,value):
        pass