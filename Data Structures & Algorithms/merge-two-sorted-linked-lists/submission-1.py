# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        tail = head
        cur1, cur2 = list1, list2
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                tail.next = cur1
                cur1 = cur1.next
            elif cur1.val >= cur2.val:
                tail.next = cur2
                cur2 = cur2.next
            tail = tail.next
        tail.next = cur1 if cur1 else cur2

        return head.next