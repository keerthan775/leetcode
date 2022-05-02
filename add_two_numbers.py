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
        print("No data")
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

ll1 = insert_rear([9,9,9,9,9,9,9])
ll2 = insert_rear([9,9,9,9])
print(get_list(ll1))
print(get_list(ll2))

def addTwoNumbers(l1, l2):
    l = []
    rem = 0
    temp1 = l1
    temp2 = l2
    while temp1 or temp2:
        if temp1 and temp2:
            sum = temp1.val + temp2.val + rem
            value = sum
            if sum >= 10:
                rem = sum // 10
                value = sum%10
            else:
                rem = 0
            l.append(value)
            temp1 = temp1.next
            temp2 = temp2.next
        elif temp2:
            sum = temp2.val + rem
            value = sum
            if sum >= 10:
                rem = sum // 10
                value = sum % 10
            else:
                rem = 0
            l.append(value)
            temp2 = temp2.next
        elif temp1:
            sum = temp1.val + rem
            value = sum
            if sum >= 10:
                rem = sum // 10
                value = sum % 10
            else:
                rem = 0
            l.append(value)
            temp1 = temp1.next

    if rem:
        l.append(rem)
    list_node = ListNode(l[0])
    temp3 = list_node
    for i in l[1:]:
        node = ListNode(i)
        temp3.next = node
        temp3 = temp3.next
    return list_node

ll = addTwoNumbers(ll1,ll2)
print(get_list(ll))