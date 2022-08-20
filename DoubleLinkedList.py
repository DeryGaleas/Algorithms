
class Node():
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList():
    
    def __init__(self):
        self.head = None

    #a -> b -> c
    def insert_at_beginning(self, data):  
        if self.head is None:
            node = Node(data=data, next=self.head, prev=None)
            self.head = node
            return
        
        node = Node(data=data, next=self.head, prev=None)
        self.head.prev = node
        self.head = node


    def insert_at_the_end(self, data):
        if self.head is None:
            self.head = Node(data=data, next=None, prev=None)
            return
    
        itr = self.head

        while itr.next:
            itr = itr.next
        
        node = Node(data=data, next=None, prev=itr)
        itr.next = node

    def insert_values(self, data_list):

        for data in data_list:
            self.insert_at_the_end(data=data)


    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count +=1;
            itr = itr.next
        return count

    def insert_values_at_index(self, index, data):
        length = self.get_length()
        if length < index or index <=0:
            raise Exception("The index provided is invalid")

        if index == 1:
            self.insert_at_beginning(data)
            return

        if index == length:
            self.insert_at_the_end(data)
            return

        itr=self.head
        count=0
        temp_node=None
        while itr:
            count+=1
            if count == index - 1:
                temp_node = itr.next
                itr.next = Node(data=data, next=temp_node, prev=itr)
                temp_node.prev = itr.next
                break
            
            itr = itr.next

    def remove_last_element(self):
        length = self.get_length()
        itr = self.head
        count = 0

        while itr:
            count +=1
            if count == length -1:
                itr.next = None
                return
            itr = itr.next
        

    def remove_at(self, index):
        length =self.get_length()
        if index <=0 or index > length:
            raise Exception("Index provided is invalid")

        if index == 1:
            self.head = self.head.next
            self.head.prev = None
            return

        if index == length:
            self.remove_last_element()
            return

        itr = self.head
        count = 0
        temp_node = None
        while itr:
            count +=1
            if count == index-1:
                itr.next = itr.next.next
                itr.next.prev = itr
                return
            itr = itr.next

    
    def remove_by_value(self, data):

        itr = self.head
        prev_node = None

        while itr:
            if itr.data == data:
                if itr == self.head:
                    self.head = self.head.next
                    self.head.prev = None
                    break
                prev_node.next = itr.next
                prev_node.next.prev = prev_node
                break
            
            prev_node = itr
            itr = itr.next

    
    def insert_after_value(self, value, data):
        length = self.get_length()
        itr= self.head
        temp_node = None
        count = 0
        while itr:
            count += 1
            if itr.data == value:
                if count == length:
                    self.insert_at_the_end(data=data)
                    break
                temp_node = itr.next
                itr.next = Node(data=data, next=temp_node, prev=itr)
                temp_node.prev = itr.next
                return
            itr = itr.next
                
            

        

    def print(self):
        itr = self.head
        values=""

        while itr:
            values += str(itr.data)+ "-->"
            itr = itr.next  

        print(values)



dl = DoubleLinkedList()
dl.insert_values(["Java", "Python", "C++", "C#"])
dl.print()
dl.insert_after_value(value="C#", data="Go")
dl.print()

