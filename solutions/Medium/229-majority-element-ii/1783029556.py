class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)
        target = n//3 + 1
        INF = 10**12

        def test(can):
            return nums.count(can) >= target


        b1 = b2 = 0
        can1 = can2 = INF
        for x in nums:
            if can1 == x:
                b1+=1
            elif can2 == x:
                b2+=1
            elif b1 == 0:
                can1 = x
                b1+=1
            elif b2 == 0:
                can2 = x
                b2+=1
            else:
                b1-=1
                b2-=1

            #print("CNT/val", b1, can1, "cNT/val", b2,can2)

        out = []
        if test(can1):
            out.append(can1)
        if test(can2):
            out.append(can2)
        return out