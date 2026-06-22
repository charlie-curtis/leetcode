"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':


        '''
        nonroots = set()
        allnodes = set()

        for x in tree:
            allnodes.add(x)
            for y in x.children:
                nonroots.add(y)


        diff = allnodes ^ nonroots
        return list(iter(diff))[0]
        '''

#followup constant space solution -> same as the XOR problem where all numbers except 1 has been duplicated


        v = 0
        for x in tree:
            v^=x.val
            for y in x.children:
                v^=y.val


        for x in tree:
            if v == x.val:
                return x


        
