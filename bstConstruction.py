# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        currentNode = self
        while True :
            if value < currentNode.value :
                if currentNode.left == None :
                    currentNode.left = BST(value)
                    break
                else :
                    currentNode = currentNode.left
            else :
                if currentNode.right == None : 
                    currentNode.right = BST(value)
                    break
                else : 
                    currentNode = currentNode.right
                      
        return self

    def contains(self, value):
        currentNode = self
        while currentNode is not None :
            if value < currentNode.value :
                currentNode = currentNode.left
            elif value > currentNode.value : 
                currentNode = currentNode.right
            else : 
                return True
        return False
       
#removal is a two step process 1= search for value to remove and remove it 
    def remove(self, value , parentNode = None):
        currentNode = self 
        while currentNode is not None : 
            if value < currentNode.value :
                parentNode = currentNode 
                currentNode = currentNode.left 
            elif value > currentNode.value : 
                parentNode = currentNode
                currentNode = currentNode.right 
            #here we find the node to be removed 
            else : 
                # ************node with two children and parentNode != None ****************
                """find the smalllest value of the right subtree and
                replace it with the node to be deleted and then remove the smallest value"""
                if currentNode.left is not None and currentNode.right is not None : 
                    #currentNode.value = smallest subTree in the right subTree of the currentNode
                    currentNode.value = currentNode.right.getMinValue() 
                    
                    #remove the smallest subtree 
                    currentNode.right.remove(currentNode.value, currentNode)  #pass currentN as a parent 

                    
                     #*************case of a node with only one child *************************

                    #node with a parentNode == None (root)
                    """ remove an element with no parentNode and we have one child """

                elif parentNode is None : 
                    if currentNode.left is not None : 
                        # replace the current node with it's left child node 
                        # assign both left child node children [left and right] to current Node
                        currentNode.value = currentNode.left.value 
                        currentNode.right = currentNode.left.right 
                        currentNode.left = currentNode.left.left
                    # currentNode.right is not None
                    elif currentNode.right is not None : 
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    # no parent and no children 
                    else : 
                        pass
                    
                    """ the case of removing a node with only one child and parentNode not None
                    steps : 
                     locate the currentNode child  if in the left or right ?
                     assign that currentNode child to the parentNode 
                     remove that currentNode 
                    """
                # currentNode is a left child Node 
                elif parentNode.left == currentNode: 
                     parentNode.left=  currentNode.left if currentNode.left is not None else currentNode.right 


                 # currentNode is a right child Node
                elif parentNode.right == currentNode : 
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                    
                break
        return self

    def getMinValue(self): 
        # keep traversing until reaching the left most child node 
        currentNode = self
        while currentNode.left is not None : 
            currentNode = currentNode.left
        return currentNode.value
            
    







