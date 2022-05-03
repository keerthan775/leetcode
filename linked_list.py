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