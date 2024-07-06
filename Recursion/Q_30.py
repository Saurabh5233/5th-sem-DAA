# Reverse a Linked List using recursion

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    


class LinkedList:
    def __init__(self):
        self.head = None
    
    def createNode(self,data):
        new_node = Node(data)
        self.head = new_node
        return self.head
    
    def add_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node  = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def reverseLL(self):
        if not self.head or not self.head.next:
            return self.head
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            self.head = prev
        
        
    def printList(self):
        curr = self.head
        while curr:
            print(curr.data,end = " ")
            curr = curr.next
        print("None")
        
list = LinkedList()

list.createNode(10)
list.add_end(20)
list.add_end(30)
list.add_end(40)
list.add_end(50)
list.add_end(60)
list.add_end(70)

list.printList()
list.reverseLL()
list.printList()




    