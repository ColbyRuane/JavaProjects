# 141. linked list cycle
# given the head of a linked list, determine if the linked list has a cycle in it

# understand:
#   input: 'head' head of linked list, type ListNode (implementation below)
#   output: boolean true/false
# constraints:
#   cycle node has a valid index in the linked list

# approach:
#   floyd's cycle-finding algorithm (tortoise and hare)
#   two pointers traverse linked list where one pointer is twice as fast as the other

# pseudocode:
#   tortoise and hare pointers
#   while tortoise and hare pointers are not null and while hare.next is not null
#      if tortoise == hare: return true
#      tortoise = tortoise.next
#      hare = hare.next.next
#   return false

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    tortoise = head
    hare = head
    while(tortoise is not None and
          hare is not None and
          hare.next is not None):
        
        tortoise = tortoise.next
        hare = (hare.next).next
        print(f'tortoise is {tortoise.val}, hare is {hare.val}')
        if hare == tortoise:
            return True
    return False
# time-complexity: O(N), corresponding to traversal of the linked list at least once to find a tail
# space-complexity: O(1), corresponding to auxiliary data (two pointers)

# linked list with cycle
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)
head.next.next.next.next.next = head.next

print(hasCycle(head))

