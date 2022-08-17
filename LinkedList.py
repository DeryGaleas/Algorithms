

class Node():
    def __init__(self, data=None, next=None):
        self.data=data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data=data, next=self.head)
        self.head = node

    # a -> b -> c -> d
    def insert_at_the_end(self,data):
        if self.head is None:
            self.head = Node(data=data, next=None)
            return

        last_node=self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = Node(data=data, next=None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_the_end(data)

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count +=1
            itr= itr.next
        return count

    def remove_at(self, index):
        if index<0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index ==0:
            self.head = self.head.next
            return

        count=0
        itr= self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count += 1

    
    def insert_at(self, index, data):
        if index <0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index ==0:
            self.insert_at_beginning(data)
            return

        count=0
        itr = self.head
        temp_variable= None
        while itr:
            if count == index -1:
                temp_variable = itr.next
                itr.next = Node(data=data, next=temp_variable)
                break
            itr = itr.next
            count += 1

    # a -> b -> c
    def remove_by_value(self, data):

        itr = self.head
        prev_node:self.head
        while itr:
            if itr.data == data:
                if itr == self.head:
                    self.head = self.head.next
                    break
                prev_node.next = itr.next
            prev_node = itr
            itr = itr.next


    def insert_after_value(self, after, data):

        itr = self.head
        while itr:
            if itr.data == after:
                node = Node(data=data, next=itr.next)
                itr.next = node
                break

            itr = itr.next

        

            

    def print(self):
        curr_head = self.head
        node_values = ""

        if curr_head is None:
            print("Linked list es empty")
            return

        while curr_head:
            node_values += str(curr_head.data) + '-->'
            curr_head = curr_head.next

        print(node_values)






if __name__ == '__main__':
   ll = LinkedList()
   ll.insert_values(["Strawberry", "apple", "Pera", "Orange"])
   ll.print()
   ll.remove_by_value(data="Strawberry")
   ll.print()
   ll.insert_after_value(after="Pera", data="Raspberry")
   ll.print()
