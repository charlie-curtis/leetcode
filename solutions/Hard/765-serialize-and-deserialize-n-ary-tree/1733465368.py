"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        out = []
        #preorder dfs
        def dfs(node):
            out.append(str(node.val))
            out.append('(')
            for x in node.children:
                dfs(x)
            out.append(')')

        dfs(root)
        return ''.join(out)
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        cur = deque(data)

        def dfs(cur):
            if not cur or cur[0] == ')':
                return None
            
            v = ""
            while cur[0] not in (')', '('):
                v+=cur.popleft()

            node = Node(int(v))
            if cur and cur[0] == '(':
                cur.popleft()
                while cur[0] != ')':
                    node.children.append(dfs(cur))
                cur.popleft()
            return node

        return dfs(cur)


        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))