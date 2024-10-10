class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:

        stack = [-1]
        for node,parent in nodes:
            while stack and stack[-1] != parent:
                prev = stack.pop()
            
            if not stack:
                return False
            stack.append(node)

        return True
            
        