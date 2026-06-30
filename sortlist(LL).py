class Solution(object):

    # Function to sort the linked list using Merge Sort
    def sortList(self, head):

        # Base case:
        # If the list is empty or has only one node,
        # it is already sorted.
        if not head or not head.next:
            return head

        # Initialize slow and fast pointers
        slow = head
        fast = head.next

        # Find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the linked list into two halves
        mid = slow.next
        slow.next = None

        # Recursively sort the left half
        left = self.sortList(head)

        # Recursively sort the right half
        right = self.sortList(mid)

        # Merge the two sorted halves
        return self.merge(left, right)

    # Function to merge two sorted linked lists
    def merge(self, l1, l2):

        # Create a dummy node to simplify merging
        dummy = ListNode(0)
        curr = dummy

        # Compare nodes from both lists
        while l1 and l2:

            # Choose the smaller node
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            # Move the current pointer
            curr = curr.next

        # Attach the remaining nodes
        curr.next = l1 if l1 else l2

        # Return the head of the merged list
        return dummy.next
