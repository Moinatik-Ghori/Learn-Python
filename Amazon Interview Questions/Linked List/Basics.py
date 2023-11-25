class Node:
    def __init__(self,nodeVal):
        self.nodeVal = nodeVal
        self.next = None
        print(f"Initializing the Node {nodeVal}")

class LinkedList:
    def __init__(self,head=None):
        self.head = head
        self.nextNode = None

    def display(self):
        print("-"*30,"\n", ">"*3,"Display Node Details","<"*3)
        current = self.head
        while current:
            print(f"Linked List: Node Value is {current.nodeVal}")
            current = current.next
        print("-"*30)

    def insertAtBegin(self, newNode):
        print(f"Inserting the node at the Beginning : {newNode.nodeVal}")
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = newNode
        else:
            current = self.head
        self.display()

    def insertAtLast(self,newNode):
        print(f"Inserting Node at the Last : {newNode.nodeVal}")
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = newNode
        else:
            newNode = self.head
        self.display()

    def insertAtMiddle(self,newNode,position):
        print(f"Inserting the Node at the {position} : {newNode.nodeVal}")
        count = 1
        current = self.head
        while current:
            if (count + 1) == position:
                newNode.next = current.next
                current.next = newNode
                break
            else:
                count += 1
                current = current.next
        self.display()

    def deleteNode(self,value):
        print(f"Deleting the Node with value : {value}")
        current = self.head
        if current.nodeVal == value:
            current.next = self.head
        while current:
            if current.nodeVal == value:
                break
            prev = current
            current = current.next
        prev.next = current.next
        current = None
        self.display()

e1 = Node(12)
e2 = Node(13)
e3 = Node(14)
e4 = Node(16)
e5 = Node(15)
e6 = Node(20)

l1 = LinkedList(e1)
l1.insertAtBegin(e2)
l1.insertAtBegin(e3)
l1.insertAtLast(e4)
l1.insertAtMiddle(e5,4)
l1.insertAtMiddle(e6,6)
l1.deleteNode(16)



