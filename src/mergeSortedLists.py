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

# brute force algorithm:
#   create new list out of all elements in the two lists
#   sort new list
#   return a new linked list based on the sorted list

class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

def bruteForce(first1: Node, first2: Node) -> Node:
    elements = []
    
    # append list1 elements to list
    current = first1
    while current:
        elements.append(current.value)
        current = current.next

    # append list2 elements to list
    current = first2
    while current:
        elements.append(current.value)
        current = current.next

    # empty list edge-case
    if not elements:
        return None

    # sort complete list
    elements.sort()

    # create new linkedlist out of sorted list
    temp = Node(-1)
    head = temp
    for element in elements:
        temp.next = Node(element)
        temp = temp.next
    head = head.next

    return head

# time-complexity = O((N+M) log(N+M)) where N and M correspond to the node size of each list
# space-complexity = O(N+M) where N+M correspond to the space needed to store a list of size N+M

def printList(head: Node):
    current = head
    # build list from nodes
    nodes = []

    # while a 'next' node exists
    while current:
        nodes.append(str(current.value))
        current = current.next
    
    # print list
    print(' -> '.join(nodes))

if __name__ == "__main__":
    # define test lists
    first1 = Node(1)
    first1.next = Node(2)
    first1.next.next = Node(4)
    first1.next.next.next = Node(8)
    first1.next.next.next.next = Node(9)

    first2 = Node(1)
    first2.next = Node(3)
    first2.next.next = Node(5)
    first2.next.next.next = Node(8)
    first2.next.next.next.next = Node(10)

    printList(bruteForce(first1, first2))