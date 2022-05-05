from linked_list import *

head = insert_rear([1,2,3,4])

def swapPairs(head):
    if not head:
        return ListNode('')
    if not head.next:
        return head

    t1 = head
    