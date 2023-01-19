class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None
		self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data): 
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
            self.head = new_node
    
    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
        return

    def insert_velues(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count=0
        itr = self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def printList(self):
        node=self.head
        print("\nTraversal in forward direction") 
        while node:
            print(f"{node.prev} - {node.data} - {node.next} ")
            last = node
            node = node.next
        print("\nTraversal in reverse direction")
        while last:
            print(f"{last.prev} - {last.data} - {last.next} ")
            last = last.prev 

    def remove_at(self,index):
        if index<0 or index>= self.get_length():
            raise Exception('Invalid Index')
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count == index - 1:
                itr.next=itr.next.next
                itr.next.prev = itr.prev.next # change requier
                break
            itr=itr.next
            count+=1

    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception('Invalid Index')
        if index==0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data)
                node.next=itr.next
                node.prev=itr.prev.next
                itr.next = node
                itr.next.next.prev =itr.next
                break
            itr = itr.next
            count += 1
    
    def add_at(self,loc,data):
        count=0
        itr=self.head
        while itr:
            if itr.data==loc:
                self.insert_at(count,data)
                return
            itr=itr.next
            count+=1
        raise Exception('location is invalid')

    def remove_the(self,loc):
        count=0
        itr=self.head
        while itr:
            if itr.data==loc:
                self.remove_at(count)
                return
            itr=itr.next   
            count+=1
        raise Exception('location is invalid')

if __name__ == "__main__":
    llist = DoublyLinkedList()
    llist.insert_velues([1,2,3,3,4,5,6,7,8,9])
    print(llist.get_length())
    print("Created DLL is: ", end =" ")
    llist.printList() 
    llist.insert_at(3,8)
    llist.add_at(8,9)
    llist.remove_the(5)
    llist.printList()