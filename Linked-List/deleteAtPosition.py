class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def printList(self):
        temp = self.head

        while(temp):
            print(temp.data , end=" => ")
            temp = temp.next

    def deleteNodeAtPosition(self, pos):

        if(self.head is None):
            return
        
        temp = self.head

        if(pos == 0):
            self.head = temp.next
            temp = None
            return
        
        for i in range(pos-1):      # it travel to postion 3 means  0 -> 1 -> 2
            if(temp is None):
                return 
            temp = temp.next
            
        if(temp is None):
            return print('There is no list')
        if(temp.next is None):
            return print('There is no Further list')
        
        nextNode = temp.next.next

        temp.next = None

        temp.next = nextNode

if __name__ == '__main__':

    llist = LinkedList()

    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)

    print("List before deletion")
    llist.printList()

    llist.deleteNodeAtPosition(4)

    print("\nList after deleting at postion 1")
    llist.printList()