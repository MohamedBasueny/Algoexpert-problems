
# This is the class of the input tree. Do not edit.

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree, target):
    # make a helper fun to pass the root 
    return findClosestValueInBstHelper(tree,target,tree.value)

def findClosestValueInBstHelper(tree, target , closet):
     # 1st call on the root
    currentNode = tree
    while currentNode is not None  :
        #updating history 
        if abs(target - closet) > abs(target - currentNode.value):
            closet = currentNode
        # excessive cases for while loop
        #by updating currentNode until reaches a None tree
        if target > currentNode.value :
            currentNode = currentNode.right
        elif target < currentNode.value :
            currentNode = currentNode.left
        else : # here we terminate the loop 
            break

    return closet
        









        if target < currentNode.value : 
            if tree.left.value is not None :
                if abs(tree.left.value - target ) < abs(tree.value - target) : 
                    closet = tree.left
                    return findClosestValueInBst(closet ,target )

                    

        elif target > tree.value : 
            if tree.right is not None :
                if abs(tree.right.value - target) < abs(tree.value - target) : 
                    closet = tree.right
                    return findClosestValueInBst(closet ,target )
        





 




   

    








    pass













