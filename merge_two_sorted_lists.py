from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def get_list(linked_list):
    temp = linked_list
    l = []
    while(temp):
        l.append(temp.val)
        temp = temp.next
    return l

def insert_rear(l):
    if not l:
        print("No val")
        return []
    elif len(l) == 1:
        return ListNode(l[0])
    else:
        linked_list = ListNode(l[0])
        temp = linked_list
        for i in l[1:]:
            node = ListNode(i)
            temp.next = node
            temp = temp.next
        return linked_list

l1 = insert_rear([-9,3])
l2 = insert_rear([5,7])

def mergeTwoLists(list1, list2):
    list3 = ListNode(0)
    t1 = list1
    t2 = list2
    t3 = list3
    if not list1 and not list2:
        return []
    elif not list1 and list2:
        return list2
    elif list1 and not list2:
        return list1
    while t1 and t2:
        if t1.val < t2.val:
            
                t3.next = ListNode(t1.val)
                t3 = t3.next
                t3.next = ListNode(t2.val)
        else:
            
                t3.next = ListNode(t2.val)
                t3 = t3.next
                t3.next = ListNode(t1.val)
            
        t3 = t3.next
        t1 = t1.next
        t2 = t2.next

    while t1:
        if t1.val < t3.val:
            t3.next = ListNode(t1.val)
            t3 = t3.next
        else:
            temp_val = t3.val
            t3.val = t1.val
            t3.next = ListNode(temp_val)
            t3 = t3.next
        t1 = t1.next

    while t2:
        if t2.val > t3.val:
            t3.next = ListNode(t2.val)
            t3 = t3.next
        else:
            temp_val = t3.val
            t3.val = t2.val
            t3.next = ListNode(temp_val)
            t3 = t3.next
        t2 = t2.next
    
    
    return list3.next




print(get_list(l1),get_list(l2))
result_list = mergeTwoLists(l1,l2)
print(get_list(result_list))

