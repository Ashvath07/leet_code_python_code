# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0,head)
        curr = head
        total =0
        while curr:
            total +=1
            curr = curr.next
        curr = dummy
        for i in range(total-n):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next
        