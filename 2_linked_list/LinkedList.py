import random


class LinkedListNode:
    """
    A single node of a linked list
    """
    def __init__(self, val, next_node=None, prev_node=None):
        """

        :param val: Value of the node
        :param next_node:
        :param prev_node:
        """
        self.val = val
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.val)


class LinkedList:
    """
    Implementation of a singly linked list
    """
    def __init__(self, values=None):
        """
        :param values: Initialize the linked list with these values
        """
        self.head = None
        self.tail = None
        if values:
            self.add_multiple(values)

    def add_multiple(self, values):
        """
        Add multiple values in the linkedList
        :parameter values--> values that will be inserted into the linkedlist
        """
        for val in values:
            self.add(val)

    def add(self, val):
        """
        Add a single value in the linked list
        :param val:
        :return:
        """
        # Create new node
        node = LinkedListNode(val)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            # Save this node as tail
            self.tail = node
        return node

    def generate(self, n, minValue, maxValue):
        """
        Populate linked list with random value
        :param n: Number of items
        :param minValue: Minimum value of the linked list
        :param maxValue: Maximum value of the the linked list
        :return:
        """
        self.head = self.tail = None
        for _ in range(n):
            self.add(random.randint(minValue, maxValue))

    def add_to_beginning(self, val):
        """
        Add a new node at the head of the linked list
        :param val:
        :return:
        """
        if not self.head:
            self.head = self.tail = LinkedListNode(val)
        else:
            self.head = LinkedListNode(val, self.head)

    def __len__(self):
        length = 0
        curr_node = self.head
        while curr_node:
            length += 1
            curr_node += curr_node.next
        return length

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return " -> ".join(values)


class DoublyLinkedList(LinkedList):
    """
    Implementation of a doubly linked list
    """
    def add(self, val):
        """
        Add new elements at the end of the linked list
        :param val:
        :return:
        """
        if not self.head:
            self.head = self.tail = LinkedListNode(val)
        else:
            self.tail.next = LinkedListNode(val, prev_node=self.tail)
            self.tail = self.tail.next

    def add_to_beginning(self, val):
        """
        Add new element at the beginning of the linked list
        :param val:
        :return:
        """
        if not self.head:
            self.head = self.tail = LinkedListNode(val)
        else:
            self.head.prev = LinkedListNode(val, next_node=self.head)
            self.head = self.head.prev

    def __str__(self):
        values = [str(x) for x in self]
        return " <-> ".join(values)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.generate(10, 1, 100)
    ll.add_to_beginning(10)
    ll.add(100)
    print(ll)
