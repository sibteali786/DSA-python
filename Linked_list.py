class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Lined List is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None) # because last element points to none
            return
        itr = self.head
        while itr.next: # until there is some next element otherwise stop if none
            itr = itr.next
        # since we are now at last element
        itr.next = Node(data,None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:  # until we get none
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next   # if index = 2 then being at 1 we now point 1 --> 3
                break
            itr = itr.next
            count += 1

    def insert_at(self,index,data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_begining(data)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)  # if we are inserting at 2 then being at 1 we point 2 --> 3 and 1 to --> 2 now
                itr.next = node
                break
            itr = itr.next
            count += 1
if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(89)
    # ll.insert_at_end(12)
    # ll.insert_at_end(32)
    # ll.insert_at_end(79)
    ll.insert_values( ['spider man','thor','hulk','iron man','captain america'])
    ll.print()
    ll.remove_at(2)
    ll.insert_at(0,"What")
    ll.insert_at(3, "Hey")
    print(ll.get_length())
    ll.print()
