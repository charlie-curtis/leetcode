# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':

        fakeHead = PolyNode()
        cur = fakeHead

        while poly1 or poly2:

            tmp = PolyNode()
            if not poly1 or (poly2 and poly2.power > poly1.power):
                tmp.coefficient = poly2.coefficient
                tmp.power = poly2.power
                poly2 = poly2.next
            elif not poly2 or (poly1 and poly1.power > poly2.power):
                tmp.coefficient = poly1.coefficient
                tmp.power = poly1.power
                poly1 = poly1.next
            elif poly1.power == poly2.power:
                tmp.coefficient = poly1.coefficient + poly2.coefficient
                tmp.power = poly2.power
                poly1 = poly1.next
                poly2 = poly2.next
            else:
                raise ValueError("what case did I miss?")
            
            if tmp.coefficient != 0:
                cur.next = tmp
                cur = cur.next
        return fakeHead.next
            





        
        