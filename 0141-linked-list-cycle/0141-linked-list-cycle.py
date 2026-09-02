# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        speed = head
        brake = head
        while speed and speed.next:
            brake = brake.next
            speed = speed.next.next
            if brake == speed:
                return True
        return False