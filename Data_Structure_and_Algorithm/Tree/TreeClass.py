class TreeNode(object):
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
        self.root = TreeNode(rootValue)
    def treeHeight(self,node):
        if not self.root:
            return 0
        leftHeight = self.treeHeight(self.root.left)
        rightHeight = self.treeHeight(self.root.right)
        return max(leftHeight,rightHeight) + 1
     
    def insertNode(self,value):
        pass

    def searchNode(self,value):
        pass

    def changeNode(self,value):
        pass
    def deleteNode(self,value):
        pass