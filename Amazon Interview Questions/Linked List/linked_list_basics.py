class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next= next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        if self.head == None:
            print("Linked List is Empty")
            return
        current_node = self.head
        node_list = ''
        while current_node:
            node_list += str(current_node.data) + "-->"
            current_node=current_node.next
        print(node_list)

    def insert_at_beginning(self,new_data):
        # Creating the Node
        new_node = Node(new_data,self.head)

        # Assigning the new node to current node.
        self.head = new_node

    def insert_at_end(self,new_data):
        # if there is no nodes present then it will create the new node.
        if self.head == None:
            self.head = Node(new_data,None)
            return
        # Assigning the first node to current_node
        current_node = self.head
        # Iterating until we find the last node
        while current_node.next:
            current_node = current_node.next
        # Assigning the  new node to last node which we found in previous iteration
        current_node.next = Node(new_data,None)

    def insert_values(self,data_values):
        self.head = None
        for data in data_values:
            self.insert_at_end(data)

    def get_couunt(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def remove_at_position(self, position):
        count=0
        current_node = self.head
        totol_nodes = self.get_couunt()
        if position > totol_nodes:
            print("Incorrect position")
            return
        if position == 0:
            self.head = current_node.next
            print(f"Deleting Node : {current_node.data}")
            return
        while current_node:
            if position == count:
                print(f"Deleting Node : {current_node.data}")
                previous_node.next = current_node.next

            previous_node = current_node
            current_node = current_node.next
            count +=1

    def insert_at_position(self,position, data):
        new_node = Node(data,None)
        count =0
        current_node = self.head
        total_length = self.get_couunt()
        if position < 0 or position > total_length:
            print(f"Incorrect Position")
            return
        if position == 0:
            self.head = new_node
            new_node.next = current_node
            return
        if position == total_length:
            self.insert_at_end(data)
            return
        while current_node:
            if count == position:
                previous_node.next = new_node
                new_node.next = current_node
            count += 1
            previous_node = current_node
            current_node = current_node.next

if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_beginning(54)
    llist.print_linked_list()

    llist.insert_at_end(9)
    llist.print_linked_list()

    llist.insert_at_beginning(31)
    llist.print_linked_list()

    llist.insert_at_beginning(1)
    llist.print_linked_list()

    llist.insert_at_end(5)
    llist.print_linked_list()

    llist.insert_values(["A","B","C","D","E"])
    llist.print_linked_list()
    print(llist.get_couunt())

    nodes = (2,9,3,4,78,99)
    llist.insert_values(nodes)
    llist.print_linked_list()

    #llist.remove_at_position(0)
    #llist.print_linked_list()

    llist.insert_at_position(6,900)
    llist.print_linked_list()


