# Data Structures Implementations in Python

This repository contains the implementation of fundamental data structures in Python: `Node`, `Stack`, `Queue`, and `DoublyLinkedList`. They were made from scraps of my labs in the university. Feel free to use them however you like.

## Node

The `Node` class is the building block for linked data structures. Each node contains:

- `value`: The data stored in the node.
- `next`: A reference to the next `Node` in the sequence.
- `prev`: A reference to the previous `Node` (used in doubly linked lists).

## Stack

The `Stack` class represents a stack data structure with Last In, First Out (LIFO) behavior, with the following operations:

- `is_empty()`: Check if the stack is empty.
- `push()`: Add a new `Node` with the provided value to the top of the stack.
- `pop()`: Remove and return the value from the top of the stack.
- `peek()`: Return the value from the top without removing it.
- `size()`: Return the number of items in the stack.

## Queue

The `Queue` class represents a queue data structure with First In, First Out (FIFO) behavior, with the following operations:

- `is_empty()`: Check if the queue is empty.
- `enqueue()`: Add a new `Node` with the provided value to the end of the queue.
- `dequeue()`: Remove and return the value from the front of the queue.
- `size()`: Return the number of items in the queue.

## DoublyLinkedList

The `DoublyLinkedList` class represents a doubly linked list, allowing insertion and deletion of nodes from both ends efficiently, with the following operations:

- `is_empty()`: Check if the list is empty.
- `append()`: Add a new `Node` with the provided value to the end of the list.
- `insertBefore()`: Insert a `Node` before a given node in the list.
- `insertAfter()`: Insert a `Node` after a given node in the list.
- `remove()`: Remove the first `Node` with the provided value from the list.
- `remove_node()`: Remove the specified `Node` from the list.
- `__str__`: Return a string representation of the list's values.

The data structures are implemented to provide basic functionality and serve as a foundation for more complex algorithms and applications.
