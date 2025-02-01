class Solution:
    def reformatDate(self, date: str) -> str:

        d, m, y = date.split(" ")

        
        A = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        d1 = ""
        for x in d:
            if x.isdigit():
                d1+=x

        if len(d1) == 1:
            d1 = "0" + d1
        b =  str(A.index(m)+1)
        if len(b) == 1:
            b = "0" + b
        return y + "-" + b + "-" + d1