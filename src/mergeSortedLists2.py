# 21. merge two sorted lists
# given the heads of two sorted linked lists list1 and list2
# merge the two lists into one sorted list. the list should be made by splicing together
# the nodes of the first two lists
# return the head of the merged linked list

# understand:
#   input: two sorted lists
#   output: one sorted list

# constraints:
#   number of list nodes in range [0, 50]
#   list node values in range [-100, 100]
#   both lists are sorted in non-decreasing order

# new approach:
#   create a new linked list. traverse through both linked lists through two pointers and compare the
#   node values at each pointer traversal. run until 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# add element to linked list and increment pointer of whichever node had a smaller value
def addToList(temp: ListNode, current: ListNode):
    temp.next = ListNode(current.val)
    current = current.next
    temp = temp.next
    return temp, current

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # define two pointers
    current1 = list1
    current2 = list2
    # dummy list head
    temp = ListNode(-101)
    head = temp

    # empty linked lists edge case
    if(not current1 and not current2):
        return None

    # while either list has elements, run through the lists
    while(current1 or current2):

        # if list1 no longer has elements
        if(not current1):
            temp, current2 = addToList(temp, current2)
        # elif list2 no longer has elements
        elif(not current2):
            temp, current1= addToList(temp, current1)
        else:
            # list1 element is smaller or equal, add to linked list
            if (current1.val <= current2.val):
                temp, current1 = addToList(temp, current1)

            # list2 element is smaller, add to linked list
            else:
                temp, current2 = addToList(temp, current2)
    
    # when all nodes have been traversed, return new linked list
    head = head.next
    return head

# time complexity = O(N+M), corresponding to both input lists being completely traversed to
#   produce the new linked list
# space complexity = O(1) of auxiliary data, O(N+M) if considering space of output list

def printList(head: ListNode):
    current = head
    # build list from nodes
    nodes = []

    # while a 'next' node exists
    while current:
        nodes.append(str(current.val))
        current = current.next
    
    # print list
    print(' -> '.join(nodes))


# head1 = head2 = None

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

printList(mergeTwoLists(head1, head2))