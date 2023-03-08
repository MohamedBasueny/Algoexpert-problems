# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        #empty linked list 
        if self.head is None: 
            self.head = node 
            self.tail = node 
            return
        else : 
            self.insertBefore(self.head , node)

    def setTail(self, node):
        if self.tail is None : 
            self.setHead(node)
        else : 
            self.insertAfter(self.tail , node )


    def insertBefore(self, node, nodeToInsert):
        # insert a node before itself can't happen ( there is only one node and it's also nodetoInsert)
        if nodeToInsert == self.head and nodeToInsert == self.tail : 
            return 
        #remove it from it's location if it exists 
        self.remove(nodeToInsert)
        # case of inserting before a head node 
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node 
        # updating head node 
        if node.prev is None : 
            self.head = nodeToInsert
        else : 
            node.prev.next  = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail : 
           return 
        self.remove(nodeToInsert)
        nodeToInsert.prev  = node 
        nodeToInsert.next  = node.next 
        if node.next is None : # tail node 
            self.tail = nodeToInsert
        else : 
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1 : # inserting at the head 
            self.setHead(nodeToInsert)
            return
        #start travrsing the ll until the tail or u at the desired position to insert at 
        node = self.head 
        currentPosition = 1 
        while node is not  None and currentPosition != position : 
            node = node.next 
            currentPosition += 1 
        # if we only hit the desires position 
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        #we are the tail node 
        else : 
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        """start searching from the head , use a temp node and then remove the desired node ,
        the temp node is used to save the connection between the nodes , so we don;t get lost 
        """
        node = self.head # start traversing from head 
        while node is not None:  
           nodeToRemove  = node 
           node = node.next 
           if nodeToRemove.value == value : 
                self.remove(nodeToRemove) 

    def remove(self, node):
        if node is self.head : 
            self.head = node.next  #assign the new head node before removing it 
        elif node is self.tail : 
            self.tail = node.prev  #assign the new tail node before removing it 
        self.removeBindings(node)
     

    def removeBindings(self,node ) : 
        """make sure to update the neighbor nodes bindings before removing the node"""
        if node.prev is not None :  
            node.prev.next = node.next 
        if node.next is not None :
            node.next.prev = node.prev
        node.next = None 
        node.prev = None

    def containsNodeWithValue(self, value):
        #starting from head node 
        node = self.head 
        # keep traversing until we reach the tail or find out value 
        while node is not None: #head & tail node is none 
            if node.value == value : 
                return True 
            # updating the node to be the next node to the right 
            node = node.next
        #didn't return any value from searching 
        return False
