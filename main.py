class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None  
        self._size = 0

    def is_empty(self):
        return self.head is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node 
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        current_head = self.head
        self.head = self.head.next
        self._size -= 1
        return current_head.value

    def peek(self):
        if self.is_empty():
            raise Exception("Пустой стек")
        return self.head.value

    def size(self):
        return self._size

class Queue:
    def __init__(self):
        self.head = None  
        self.tail = None  
        self._size = 0

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            # If queue is empty first element is a head and a tail
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Очередь пуста")
        current_head = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return current_head.value

    def size(self):
        return self._size

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  

    def is_empty(self):
        """Проверяет, пуст ли список."""
        return self.head is None

    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            # If list is empty then a new node become head
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node

    def insertBefore(self, node, node_to_insert):
        if node_to_insert == None or node == None:
            return

        node_to_insert.prev = node.prev
        node_to_insert.next = node

        # if not was head changing head
        if node.prev is None:
            self.head = node_to_insert
        else:
            node.prev.next = node_to_insert

        node.prev = node_to_insert

    def insertAfter(self, node, node_to_insert):
        if node_to_insert == None or node == None:
            return

        node_to_insert.prev = node
        node_to_insert.next = node.next

        # if node was tail changing tail
        if node.next is None:
            self.tail = node_to_insert
        else:
            node.next.prev = node_to_insert

        node.next = node_to_insert

    def remove(self, value):
        """Удаляет узел с заданным значением из списка."""
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return True  # Узел найден и удален
            current = current.next
        return False  # Узел не найден

    def remove_node(self, node_to_remove):
        if node_to_remove == self.head:
            self.head = node_to_remove.next
            if self.head:
                self.head.prev = None
        else:
            node_to_remove.prev.next = node_to_remove.next

        if node_to_remove == self.tail:
            self.tail = node_to_remove.prev
            if self.tail:
                self.tail.next = None
        else:
            node_to_remove.next.prev = node_to_remove.prev

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return str(values)
