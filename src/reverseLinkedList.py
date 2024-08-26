# 206. reverse linked list
# given the head of a singly linked list, reverse the list and return the reversed list

# understand:
#   input: 'head' head of linked list, type ListNode
#   output: head of reverse linked list, type ListNode
# constraints:
#   number of nodes [0, 5000]

# intuition:
#  - determine number of nodes in linked list
#  - iterate through list and switch current and current.next node until reach end
#  - when reach end, decrease traversal length by 1 (so final node is not switched)
#  OR
#  - iterate through linked list, reverse pointers of existing nodes
#  - when reach end, return the final node as it is technically the head

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList3(head):
    # empty list edge-case
    if not head: return None
    # single element edge case
    if not head.next: return head

    # determine length of list
    current = head
    length = 0
    while current != None:
        length += 1
        current = current.next

    current = head
    while not (length == 1):
        while current != None:
            current, current.next = current.next, current
            current = current.next
        length -= 1
    return head
# TIME LIMIT EXCEEDED!

def reverseList2(head):
    # empty list edge-case
    if not head: return None
    # single element edge case
    if not head.next: return head

    current = head
    previous = None
    while current:
        # store next node
        next = current.next
        # reverse current node's next pointer
        current.next = previous
        # move pointers
        previous = current
        current = next
    return previous

def reverseList(head):
    now = head
    prev = None
    while now:
        next = now.next
        now.next = prev
        prev, now = now, next
    return prev
# time-complexity: O(N) corresponding to traversal of linked list
# space-complexity: O(N) corresponding to auxiliary data (pointers)
