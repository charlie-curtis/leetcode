"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return None
        def sVal(v, lvl, pos):
            out = 0
            for i in range(14):
                
                if v&1:
                    out|=(1<<i)
                if pos&1:
                    out|=(1<<(i+14))
                if lvl&1:
                    out|=(1<<(i+28))
                v>>=1
                pos>>=1
                lvl>>=1
            return out

        out = None
        q = deque()
        q.append([root, -1, -1])

        lvl = 0
        while q:
            n = len(q)
            for i in range(n):
                node,prevlvl, prevpos = q.popleft()
                #print("processing", node.val, "and my parents were", prevlvl, prevpos)
                newnode = TreeNode(sVal(node.val, prevlvl, prevpos))
                if not out:
                    out = [newnode]
                else:
                    out[-1].left = newnode
                    out.append(newnode)
                for x in node.children:
                    #print("enqueuing child", x.val, "with parent level/pos", lvl, i)
                    q.append([x, lvl, i])
            lvl+=1

        t = out[0]
        while t:
            #print("found when serializing", t.val)
            t = t.left
        #print('END')
        #print()
        return out[0]



        
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return None


        '''
        10 bits for height
        14 bits for pos
        14 bits for val
        
        bit pos 0-13 = val
        bit pos 14-27 = pos
        bit pos 28-37 = height
        '''

        def dVal(x):

            v = 0
            for i in range(14):
                if x&(1<<i) > 0:
                    v|=(1<<i)
            pos = 0
            for i in range(14,28):
                if x&(1<<i) > 0:
                    pos|=(1<<(i-14))
            h = 0
            for i in range(28,37):
                if x&(1<<i) > 0:
                    h|=(1<<(i-28))
            return [v, h, pos]

        root = data
        d = {}
        q = deque()
        q.append(root)
        out = None
        seen = Counter()
        while q:
            node = q.popleft()
            val, parentlevel, parentpos = dVal(node.val)
            #print("VAL WAS", val, "and parents were", parentlevel, parentpos)
            newnode = Node(val)
            newnode.children = []
            if not out:
                out = newnode
                #print("init root of new tree")
                d[(0,0)] = newnode
            else:
                kkey = (parentlevel, parentpos)
                parent = d[kkey]
                parent.children.append(newnode)
                #print("attching a node with a val of ", newnode.val, "to parent", parentlevel, parentpos)

                mylevel = parentlevel+1
                mypos = seen[mylevel]
                seen[mylevel]+=1
                d[(mylevel,mypos)] = newnode
                #print("my level/pos was", mylevel, mypos)
            if node.left:
                q.append(node.left)

        #print("returning")
        return out

        

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))