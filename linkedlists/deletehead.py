# Delete head of DLL
# Given the head of a doubly linked list, remove the node at the head of the linked list and return the head of the modified list.
# The head is the first node of the linked list.
# Examples:
# Input: head -> 1 <-> 2 <-> 3
# Output: head -> 2 <-> 3
# Explanation:
# The node with value 1 was removed.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def deleteHead(self, head):
        if not head:
            return None
        newhead = head.next
        if newhead is not None: 
            newhead.prev = None
        return newhead

# If the DLL is empty → return None.
# Set new_head to head.next.
# If new_head exists, break its connection with the old head.
# Return new_head.


