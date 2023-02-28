# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sum_list = []
    branchSumsHelper(root,0,sum_list)
    return sum_list

def branchSumsHelper(node,runningSum,sum_list) :  
    #base case 
    if node is None : 
       return #does no thing to a None node 
    # manipulate the  input without changing it  
    newRunningSum = runningSum +  node.value

    if node.left is None and node.right is None :#leaf node case 
        sum_list.append(newRunningSum)
        return    

    branchSumsHelper(node.left, newRunningSum,sum_list)
    branchSumsHelper(node.right, newRunningSum, sum_list)
    



