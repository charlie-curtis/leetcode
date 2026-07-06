class Solution:
    def minFlips(self, g: List[List[int]]) -> int:

        m,n = len(g), len(g[0])

        #so if i set (0,0) to a value, then i also have to set (0,n-1), (m-1, n-1), and (m-1,0) to the same value

        # x x x x
        # x x x x
        # x x x x

        #1,0,0]
        #[0,1,0]
        #[0,0,1]

        cost = 0
        seen = set()
        debug = Counter()
        addOnes = defaultdict(list)
        total = 0
        for i in range(m):
            for j in range(n):
                if n-1-j < j or m-1-i < i:
                    continue
                a = (i,j) #top leftk
                b = (i, n-1-j) #top right
                c = (m-1-i, j) #bottom left
                d = (m-1-i, n-1-j) #bottom right

                sset = set([a,b,c,d])
                C = Counter({0:0, 1:0})
                for x,y in sset:
                    C[g[x][y]]+=1
                ones = C[1]
                zeros = C[0]

                #print(C, sset)

                #the sizes of these sets is either 1,2,4, but 4 is useless

                if zeros == 0 or ones == 0:
                    #print("A")
                    #already in desired state
                    if ones > 0:
                        total+=ones
                        addOnes[4-ones].append(ones)
                    else:
                        #we are not adding 1s now, but can convert in the future
                        addOnes[zeros].append(zeros)

                elif ones < zeros:
                    #print("B")
                    #we are choosing 0's
                    cost+=ones
                    if ones + zeros == 2:
                        addOnes[2].append(2)
                    elif ones + zeros == 1:
                        #right now, we are choosing to keep a 0, but can change that in the future to a 1
                        addOnes[1].append(1)
                elif ones > zeros:
                    #print("C")
                    #we are choosing 1s
                    cost+=zeros
                    total+=ones+zeros
                    if ones + zeros == 2:
                        addOnes[2].append(2)
                    elif ones + zeros == 1:
                        #right now, we are choosing to keep a 1, but can change that in the future to simulate subtracting 1 by adding 3 (mod 4)
                        addOnes[3].append(1)
                elif ones == zeros:
                    #print("D")
                    cost+=zeros
                    #keep zeros
                    #we can 
                    addOnes[ones+zeros].append(0)
                #print("TOTAL", total)

                        
        addOnes[1].sort()
        addOnes[2].sort()
        addOnes[3].sort()
        #print(addOnes)
        #print("total", total)
        if total % 4 == 0:
            #print("h1")
            return cost
        if total % 4 == 3:
            #print("h2")
            options = [10**9]
            if len(addOnes[1]):
                options.append(addOnes[1][0])
            if len(addOnes[2]) and len(addOnes[3]):
                options.append(addOnes[2][0] + addOnes[3][0])
            return cost + min(options)
        if total % 4 == 2:
            #print("h3")
            return cost + addOnes[2][0]
        if total % 4 == 1:
            #print("h4")
            #need to add 3
            return cost + addOnes[3][0]
        return cost

        #[1,0,0]
        #[0,1,0]
        #[0,0,1]
 
        #[0,0,0]
        #[0,1,0]
        #[0,0,0]

        #2 to get palindrome, with 3 parity