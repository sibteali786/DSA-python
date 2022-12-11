class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)  # because last element points to none
            return
        itr = self.head
        while itr.next:  # until there is some next element otherwise stop if none
            itr = itr.next
        # since we are now at last element
        itr.next = Node(data, None)

    def insert_values(self, data_list):
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
                itr.next = itr.next.next  # if index = 2 then being at 1 we now point 1 --> 3
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_begining(data)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,
                            itr.next)  # if we are inserting at 2 then being at 1 we point 2 --> 3 and 1 to --> 2 now
                itr.next = node
                break
            itr = itr.next
            count += 1


# Exercise 2
class Node_Double:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node_Double(data, self.head, None)
        if self.get_length() == 0:
            self.head = node
        else:
            first = self.head
            first.prev = node
            self.head = node


    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node_Double(data, None, None)  # because last element points to none
            return
        itr = self.head
        while itr.next:  # until there is some next element otherwise stop if none
            itr = itr.next
        # since we are now at last element
        itr.next = Node_Double(data, None,itr)

    def insert_values(self, data_list):
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

    def print_forward(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ""
        while itr.next:
            itr = itr.next
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.prev
        print(llstr)

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next  # if index = 2 then being at 1 we now point 1 --> 3
                current_itr = itr
                itr = itr.next
                itr.prev = current_itr
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):

        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                next = itr.next
                node = Node_Double(data,
                            itr.next,itr)  # if we are inserting at 2 then being at 1 we point 2 --> 3 and 1 to --> 2 now
                itr.next = node
                next.prev = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            nextElement = self.head.next
            node = Node_Double(data_to_insert, nextElement, self.head)
            nextElement.prev = node

        itr = self.head
        while itr:
            if itr.next is None:
                self.insert_at_end(data_to_insert)
                break
            if itr.data == data_after:
                nextElement = itr.next
                node = Node_Double(data_to_insert, itr.next, itr)
                itr.next = node
                nextElement.prev = node
                break

            itr = itr.next

if __name__ == '__main__':
    # Exercise 1
    # ll = LinkedList()
    # ll.insert_values(["banana", "mango", "grapes", "orange"])
    # ll.print()
    # ll.insert_after_value("mango", "apple")  # insert apple after mango
    # ll.print()
    # ll.remove_by_value("orange")  # remove orange from linked list
    # ll.print()
    # ll.remove_by_value("figs")
    # ll.print()
    # ll.remove_by_value("banana")
    # ll.remove_by_value("mango")
    # ll.remove_by_value("apple")
    # ll.remove_by_value("grapes")
    # ll.print()

    dll = DoublyLinkedList()
    dll.insert_at_begining("4")
    dll.insert_at_begining("3")
    dll.insert_at_begining("2")
    dll.insert_at_begining("1")
    dll.insert_at_begining("0")
    # dll.remove_at(0)
    # dll.insert_at(3,20)
    dll.insert_after_value("0", "5")
    dll.print_forward()
    dll.print_backward()

