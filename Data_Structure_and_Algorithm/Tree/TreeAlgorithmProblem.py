class TreeNode(object):
    """
    Define a binary tree node.
    Tree.val, Tree.left, Tree.right
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def traversalTreeF(root):
    """
    Tranverse a tree.
    """
    if not root:
        return
    print (root.val, end=' ')
    traversalTreeF(root.left)
    traversalTreeF(root.right)

def traversalTreeM(root):
    """
    Tranverse a tree.
    """
    if not root:
        return    
    traversalTreeM(root.left)
    print (root.val, end = ' ')
    traversalTreeM(root.right)

def traversalTreeE(root):
    """
    Tranverse a tree.
    """
    if not root:
        return    
    traversalTreeE(root.left)
    traversalTreeE(root.right)
    print (root.val, end = ' ')

def tranversalTreeLevelOrder(root):
    if not root:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        temp = queue.pop(0)
        print (temp.val, end = ' ')
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)
        

def height_of_tree(root):
    if root == None:
        return 0
    return max(height_of_tree(root.left),height_of_tree(root.right))+1

def minDepth(root):
    if root == None:
        return 0
    if root.left == None and root.right != None:
        return minDepth(root.right)+1
    if root.left != None and root.right == None:
        return minDepth(root.left)+1
    return min(minDepth(root.left),minDepth(root.right))+1

def check_balance(root):
    if root == None:
        return True
    if abs(height_of_tree(root.left)-height_of_tree(root.right))>1:
        return False
    else:
        return check_balance(root.left) and check_balance(root.right)


def insertBST(root,value):
    if not root:
        return TreeNode(value)
    if value < root.val:
        root.left = insertBST(root.left,value)
    else:
        root.right = insertBST(root.right, value)
    return root

def searchBST(root,value):
    if not root:
        return False
    if value == root.val:
        return True 
    elif value < root.val:
        return searchBST(root.left, value)
    else:
        return searchBST(root.right, value)

def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if not nums or len(nums) == 0:
        return None                
    if len(nums) == 1:
        return TreeNode(nums[0])
    middle = len(nums)//2 
    root = TreeNode(nums[middle])
    root.left = sortedArrayToBST(nums[0:middle])
    root.right = sortedArrayToBST(nums[middle + 1:])
    return root

def leafSum(root):
    leafs = []
    leafSumHelper(root,leafs)
    return sum(leafs)

def leafSumHelper(node,leafs):
    if node == None:
        return 
    if node.left == None and node.right == None:
        leafs.append(node.val)
    
    leafSumHelper(node.left, leafs)
    leafSumHelper(node.right, leafs)

def treePath(root):
    paths = []
    treePathHelper(root,paths)

def treePathHelper(node, paths):
    if node == None:
        return 
    paths.append(node.val)
    if node.left == None and node.right == None:
        print("Path: ", paths)
    
    treePathHelper(node.left, paths)
    treePathHelper(node.right, paths)

    paths.pop()

def isIdentical(root1,root2):
    if root1 == None and root2 == None:
        return True
    elif root1 == None or root2 == None:
        return False

    if root1.val != root2.val:
        return False
    else:
        return isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)


if __name__ == "__main__":
    root = TreeNode(10)
    insertBST(root,8)
    insertBST(root,7)
    insertBST(root,12)
    insertBST(root,10)
    insertBST(root,3)
    insertBST(root,11)
    print()
    traversalTreeF(root)
    print()
    traversalTreeM(root)
    print()
    traversalTreeE(root)
    print()
    tranversalTreeLevelOrder(root)
    print()
    print("Height of Tree:", height_of_tree(root))
    print()
    print("MinDepth of Tree:", minDepth(root))
    print()
    print(searchBST(root,11))