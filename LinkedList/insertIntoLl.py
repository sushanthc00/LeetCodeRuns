class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtTheBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def insertAtTheEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


if __name__ == '__main__':   #Ctrl + J
    llist = LinkedList()

    llist.insertAtTheBeginning("finally")
    llist.insertAtTheBeginning("end")
    llist.insertAtTheBeginning("the")
    llist.insertAtTheBeginning("is")
    llist.insertAtTheBeginning("this")

    llist.insertAtTheEnd("unless")

    llist.printList()