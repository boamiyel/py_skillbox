class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def get(self, index):
        if index < 0:
            return None

        current = self.head
        i = 0
        while current:
            if i == index:
                return current.data
            current = current.next_node
            i += 1
        return None

    def remove(self, index):
        if index < 0 or not self.head:
            return

        if index == 0:
            self.head = self.head.next_node
            return

        current = self.head
        prev = None
        i = 0

        while current and i < index:
            prev = current
            current = current.next_node
            i += 1

        if current:
            prev.next_node = current.next_node

    def insert(self, index, val):
        if index < 0:
            return

        new_node = Node(val)

        if index == 0:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        prev = None
        i = 0

        while current and i < index:
            prev = current
            current = current.next_node
            i += 1

        if current:
            prev.next_node = new_node
            new_node.next_node = current

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next_node
