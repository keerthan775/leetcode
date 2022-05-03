from linked_list import *

linked_list = insert_rear([1,2,3,4,5])

def reverseBetween(head, left: int, right: int):
    l1 = []
    count1 = 0
    t1 = head
    while count1 != left-1:
        l1.append(t1.val)
        t1 = t1.next
        count1 += 1
    l2 = []
    count2 = left-1
    while count2 != right:
        l2.append(t1.val)
        t1 = t1.next
        count2 += 1
    
    l3 = []
    while t1:
        l3.append(t1.val)
        t1 = t1.next
    
    l4 = l1+l2[::-1]+l3
    output_list = ListNode('')
    temp1 = output_list
    for i in l4:
        temp1.next = ListNode(i)
        temp1 = temp1.next
    return output_list.next
    

ll = reverseBetween(linked_list,2,4)
print("---",get_list(ll))