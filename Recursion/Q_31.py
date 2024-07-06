# Merge two sorted Linked Lists using recursion

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_two_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    # Recursive case
    if l1.value < l2.value:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2
    

def print_linked_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")
    
l1 = ListNode(1, ListNode(3, ListNode(5)))

l2 = ListNode(2, ListNode(4, ListNode(6)))

merged_list = merge_two_lists(l1, l2)

print_linked_list(merged_list)
