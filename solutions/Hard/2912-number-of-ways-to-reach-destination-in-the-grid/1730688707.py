class Solution:
    def numberOfWays(self, n: int, m: int, k: int, source: List[int], dest: List[int]) -> int:

        #need to handle sources where n or m == 1
        MOD = 10**9 + 7

        @cache
        def dp(dest_row, dest_col, k):
            if k == 0 and dest_col and dest_row:
                return 1
            if k < 0:
                return 0


            ans = 0
            if dest_row:
                if dest_col: #DEST ROW AND COL
                    #destination
                    #I can either move vertically (but i move out of the dest row)
                    ans+=(n-1)*dp(False, True, k-1)
                    #Or i can move laterally (but I move out of the dest col)
                    ans+=(m-1)*dp(True, False, k-1)
                else: #DEST ROW, NOT DEST COL
                    #we are in dest row but not dest col
                    #move laterally, stay in dest_row, but don't go to dest column
                    ans+=(m-2)*dp(dest_row, dest_col, k-1)
                    #move laterally, stay in dest_row, and go to dest_col
                    ans+=dp(dest_row, True, k-1)
                    #move vertically, leave dest_row, (and we already weren't in dest_col)
                    ans+=(n-1)*dp(False, dest_col, k-1)
            elif dest_col: #DEST COL, NOT DEST ROW
                #move vertically, stay out of dest_row
                ans+=(n-2)*dp(False, True, k-1)
                #move horizontally, leave dest_col
                ans+=(m-1)*dp(False, False, k-1)
                #move vertically to dest_row
                ans+=dp(True,True, k-1)
            else: #NOT DEST ROW OR COLUMN
                #we are neither in dest_row or dest_col
                
                #move vertically, stay out of dest_row
                ans+=(n-2)*dp(False, False, k-1)
                #move hor, stay out of dest_col
                ans+=(m-2)*dp(False, False, k-1)
                #move vert to dest_row
                ans+=dp(True, False, k-1)
                #move hor to dest_col
                ans+=dp(False, True, k-1)


            return ans % MOD


        return dp(source[0] == dest[0], source[1] == dest[1], k)



