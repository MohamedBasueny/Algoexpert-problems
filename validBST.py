class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBstHelper(tree,float("-inf") , float("inf")) 


def validateBstHelper(tree ,minValue,maxValue):
    # base case [any child of a leaf node is None]
    if tree is None:  return True
    # invalid BST case 
    if tree.value < minValue or tree.value >= maxValue: 
        return False
    #keep track of the min and max value in the tree
    leftIsValid = validateBstHelper(tree.left ,minValue= minValue , maxValue= tree.value)
    return leftIsValid and validateBstHelper(tree.right, maxValue=maxValue, minValue=tree.value)
        

    


