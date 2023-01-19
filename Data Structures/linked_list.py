class Node:
   def __init__(self, data=None, next=None):
      self.data = data
      self.next = next

class LinkedList:
   def __init__(self):
      self.head = None

   def insert_at_begining(self,data):
      node = Node(data, self.head)
      self.head = node


   def print(self):
      if self.head is None:
         print('linked list is empty')
         return

      itr = self.head
      llstr = ''
      
      while itr:
         llstr += str(itr.data) +' - '+str(itr.next) + '-->' 
         itr = itr.next
      
      return llstr
   
   def insert_at_end(self,data):
      if self.head is None:
         self.head = Node(data,None)
         return
      
      itr=self.head
      while itr.next:
         itr= itr.next

      itr.next=Node(data,None)

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
            node = Node(data,itr.next)
            itr.next = node
            break

         itr = itr.next
         count += 1

   def add_at(self,loc,data):
      count=0
      itr=self.head
      while itr:
         print(itr.data)
         if itr.data==loc:
            print('we are in if')
            self.insert_at(count,data)
            return
         itr=itr.next   
         count+=1
      raise Exception('location is invalid')



if __name__ == "__main__":
   ll = LinkedList()
   ll.insert_at_end(8)
   ll.insert_at_begining(5)
   ll.insert_at_begining(88)
   ll.insert_at_end(89)

   lj = LinkedList()
   lj.insert_velues([1,2,3,4,5,6,7])
   ll.remove_at(3)
   lj.remove_at(4)
   ll.insert_at(3,'three')
   lj.insert_at(3,9)
   print(ll.print())
   print(lj.print())
   print(ll.get_length())
   print(lj.get_length())
   print(ll.print())
   print(lj.print())
   ll.add_at('three',606)
   print(ll.print())