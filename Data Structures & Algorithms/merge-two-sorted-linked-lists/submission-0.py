# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2 
        head = ListNode(0)
        tail = head 

        while p1 and p2:
            if p1.val < p2.val:
                newNode = ListNode(p1.val)
                p1 = p1.next
            else:
                newNode = ListNode(p2.val)
                p2 = p2.next
            tail.next = newNode
            tail = tail.next
            

        while p1 != None:
            newNode = ListNode(p1.val)
            p1 = p1.next
            tail.next = newNode
            tail = tail.next
            

        while p2 != None:
            newNode = ListNode(p2.val)
            p2 = p2.next
            tail.next = newNode
            tail = tail.next

        return head.next
                

        