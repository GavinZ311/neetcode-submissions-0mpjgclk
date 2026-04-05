# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Creating a new node
        dummy = ListNode(0)
        #Tail will always point to the last node in the list
        tail = dummy 

        #Pointers to iterate
        cur1, cur2 = list1, list2

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                tail.next = cur1
                cur1 = cur1.next
            else:
                tail.next = cur2
                cur2 = cur2.next
            #Move the tail pointer to the newly added node
            tail = tail.next
        
        #If one list is empty, attach the remained
        tail.next = cur1 if cur1 else cur2

        #The head of the merged list is after the dummy node
        return dummy.next