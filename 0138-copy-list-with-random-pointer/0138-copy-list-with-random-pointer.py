class Solution(object):
    def copyRandomList(self, head):

        if head is None:
            return None

        # original node -> copied node
        mp = {}

        temp = head

        # Create all new nodes
        while temp:
            mp[temp] = Node(temp.val)
            temp = temp.next

        # Connect next and random
        temp = head

        while temp:
            mp[temp].next = mp.get(temp.next)
            mp[temp].random = mp.get(temp.random)

            temp = temp.next

        return mp[head]