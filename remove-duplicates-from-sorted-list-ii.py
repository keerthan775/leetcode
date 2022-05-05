from linked_list import *

ll = insert_rear([1,2,3,3,4,4,5])

def deleteDuplicates(head):
    if not head:
        return head
    if not head.next:
        return head
    t1 = head
    d = {}
    while t1:
        if t1.val in d:
            d[t1.val] += 1
        else:
            d[t1.val] = 1
        t1 = t1.next
    print(d) 
    new_list = ListNode('')
    t1 = new_list
    for i in d:
        if d[i] == 1:
            t1.next = ListNode(i)
            t1 = t1.next
    return new_list.next
    

ll2 = deleteDuplicates(ll)
print(get_list(ll2))