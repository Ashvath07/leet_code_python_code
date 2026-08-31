class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        start =-1
        end = -1
        index = 1
        dist = float('inf')
        prev = head
        curr = head.next
        while curr.next is not None:
            if ((curr.val > prev.val and curr.val > curr.next.val)or(curr.val < prev.val and curr.val < curr.next.val)):
                if start ==-1:
                    start = index
                    end =index
                else:
                    dist = min(dist,index - end)
                    end =index
            prev = curr
            curr =curr.next
            index +=1
        if start == end:
            return [-1,-1]
        return [dist,end -start]
        