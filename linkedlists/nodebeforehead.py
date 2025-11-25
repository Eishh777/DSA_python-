# Insert node before head in DLL
# Given the head of a doubly linked list and an integer X, insert a node with value X before the head of the linked list and return the head of the modified list.
# Examples:
# Input: head -> 1 <-> 2 <-> 3, X = 3
# Output: head -> 3 <-> 1 <-> 2 <-> 3
# Explanation: 3 was added before the 1st node. Note that the head's value is changed.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None           

    def insert_before_head(head, x):
        new_node = Node(x)
        new_node.next = head
        if head is not None:
            head.prev = new_node
        head = new_node
        return head
#time complexity: O(1)
# space complexity: O(1)
# Use when u need to add a node at the beginning of a doubly linked list    