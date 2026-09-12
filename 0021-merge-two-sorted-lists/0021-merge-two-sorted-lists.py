# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        end = dummy
        while list1 and list2:
            if list1.val<list2.val:
                end.next = list1
                list1 = list1.next
            else:
                end.next = list2
                list2 = list2.next
            end = end.next
        end.next = list1 if list1 else list2
        return dummy.next
