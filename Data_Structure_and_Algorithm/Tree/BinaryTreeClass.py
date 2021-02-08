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
        return self.treeHeightHelper(self.root)
        
    def treeHeightHelper(self,root):
        if not root:
            return 0
        leftHeight = self.treeHeightHelper(root.left)
        rightHeight = self.treeHeightHelper(root.right)
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

    def changeNode(self,value1,value2):
        self.deleteNode(value1)
        self.insertNode(value2)

    def deleteNode(self,value):
        self.root = self.deleteNodeHelper(self.root,value)
    
    def deleteNodeHelper(self,root,value):
        if not root:
            return root 
        if value > root.val:
            root.right = self.deleteNodeHelper(root.right, value)
        elif value < root.val:
            root.left = self.deleteNodeHelper(root.left, value)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right

            temp = root.right 
            while temp.left:
                temp = temp.left 
            
            mini = temp.val 
            root.val = mini 
            root.right = self.deleteNodeHelper(root.right,mini)
        return root 
        

if __name__ == "__main__":
    BST = BinarySearchTree(3)
    print (BST.treeHeight())