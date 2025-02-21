class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:


        #4 7 10
        #1 2 3 7 8 9

        
        def check(a,b):
            m,n=len(a),len(b)

            #we know we need to choose a prefix
            #we can choose between 0 and m elements from the first array


            needed = (m+n)//2 + 1
            l=max(0,needed-n)
            r=min(m,needed)
            while True:
                chosen=l+(r-l)//2
                p1=p2=-1e15
                other=needed-chosen
                if chosen > 0:
                    p1 = a[chosen-1]
                if other > 0:
                    p2 = b[other-1]
                
                p3=p4=1e15
                if chosen < m:
                    p3 = a[chosen]
                if other < n:
                    p4 = b[other]
                
                if p1 > p4:
                    #we overshot on a
                    r = chosen -1
                elif p2 > p3:
                    #we overshot on b
                    l = chosen + 1
                else:
                    #this is it. we need to pick the largest value if odd, else the 2 largest values if even
                    options = []
                    if chosen > 0:
                        options.append(a[chosen-1])
                    if other > 0:
                        options.append(b[other-1])
                    if chosen > 1:
                        options.append(a[chosen-2])
                    if other > 1:
                        options.append(b[other-2])
                    options.sort()
                    if (m+n)%2:
                        return options[-1]
                    return (sum(options[-2:]))/2

            
        if len(a) > len(b):
            return check(b,a)
        return check(a,b)
        