class Solution:
    def nextPalindrome(self, num: str) -> str:

        n = len(num)
        num = [x for x in num]

        #[0,n//2-1]
        for i in range(n//2-1, 0, -1):
            if num[i] > num[i-1]:
                swap_idx = -1
                for j in range(i, n//2):
                    if num[i-1] < num[j]:
                        if swap_idx == -1 or num[swap_idx] > num[j]:
                            swap_idx = j
                num[i-1],num[swap_idx] = num[swap_idx],num[i-1]
                num[i:n//2] = sorted(num[i:n//2])
                a = num[0:n//2]
                b = a[::-1]
                if n % 2 == 1:
                    a+=num[n//2]
                return ''.join(a+b)
        return ""



        #45321

        #54123
        