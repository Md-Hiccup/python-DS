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
            print(temp.data, end=" => ")
            temp = temp.next
        
    def deleteNode(self, key):
        temp = self.head

        if(temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return
    
        while(temp is not None):
            if( temp.data == key):
                break
            prev = temp 
            temp = temp.next

        if(temp == None):
            return 
        
        prev.next = temp.next

if __name__ == '__main__':

    llist = LinkedList()

    llist.push(6)
    llist.push(3)
    llist.push(4)
    llist.push(1)
    #   It print the    1 => 4 => 3 => 6
    print("List before deletion: ")
    llist.printList()

    llist.deleteNode(3)     # Deleting node 3

    print("\nList after deleting 3")
    llist.printList()