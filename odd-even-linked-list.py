from linked_list import *

head = insert_rear([2,1,3,5,6,4,7])

def oddEvenList(head):
    t1 = head
    odd_list = ListNode('')
    odd_temp = odd_list
    even_list = ListNode('')
    even_temp = even_list
    is_odd = True
    is_even = False
    while t1:
        if is_odd:
            is_odd = False
            is_even = True
            odd_temp.next = ListNode(t1.val)
            odd_temp = odd_temp.next
        elif is_even:
            is_even = False
            is_odd = True
            even_temp.next = ListNode(t1.val)
            even_temp = even_temp.next
        t1 = t1.next
    print(get_list(even_list))
    print(get_list(odd_list))
    even_list = even_list.next
    odd_list = odd_list.next
    odd_temp.next = even_list
    return odd_list
ll = oddEvenList(head)
print(get_list(ll))