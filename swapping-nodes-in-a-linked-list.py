from linked_list import *

head = insert_rear([7,9,6,6,7,8,3,0,9,5])

def swapNodes(head, k):
    total_nodes = 0
    t1 = head
    while t1:
        total_nodes += 1
        t1 = t1.next
    print(total_nodes)
    first = head
    second = head
    t1 = head
    curr_node = 1
    while t1:
        if curr_node == k:
            first = t1
        if curr_node == total_nodes - k +1 :
            second = t1
        curr_node += 1
        t1 = t1.next
    print(first.val, second.val)
    first.val, second.val = second.val, first.val
    return head

head = swapNodes(head, 5)
print(get_list(head))