class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squi: List[int], nuts: List[List[int]]) -> int:


        def get_dst(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])
        baseline = 0
        ans = 1e10
        for x,y in nuts:
            dst = get_dst([x,y], tree)
            baseline+=2*dst

        print(baseline)

        for x,y in nuts:
            dst_to_tree = get_dst([x,y], tree)
            dst_to_squi = get_dst([x,y], squi)

            can = baseline-dst_to_tree + dst_to_squi
            ans = min(ans, can)
        return ans

        