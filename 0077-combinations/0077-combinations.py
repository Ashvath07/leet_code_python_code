class Solution(object):
    def combine(self, n, k):
        stack =[]
        def count(start,path):
            if len(path) == k:
                stack.append(path[:])
                return 
            for i in range(start,n+1):
                path.append(i)
                count(i+1,path)
                path.pop()
        count(1,[])
        return stack

        
        
        
        