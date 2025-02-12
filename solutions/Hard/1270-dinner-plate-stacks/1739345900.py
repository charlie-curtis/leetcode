from sortedcontainers import SortedDict, SortedList
class DinnerPlates:

    def __init__(self, m: int):
        self.m=m
        self.recycle=SortedList()
        self.cur=0
        self.c=SortedDict()
        self.ip=SortedDict()
        

    def push(self, val: int) -> None:
        #find a home
        r=1e15 if not self.recycle else self.recycle[0]
        p=1e15 if len(self.ip) == 0 else self.ip.peekitem(0)[0]
        c=self.cur
        
        w=min(r,p,c)
        if w in [r,c]:
            if w == c:
                self.cur+=1
            if w == r:
                del self.recycle[0]
            li=[val]
            if self.m==1:
                self.c[w] = li
            else:
                self.ip[w] = li
        elif w==p:
            li=self.ip[p]
            li.append(val)
            if len(li) == self.m:
                del self.ip[p]
                self.c[p] = li
            
                
        
        
        

    def pop(self) -> int:
        p=-1 if len(self.ip) == 0 else self.ip.peekitem(-1)[0]
        c =-1 if len(self.c) == 0 else self.c.peekitem(-1)[0]
        w = max(p,c)
        if w == -1: return w
        v=-1
        if w == p:
            li = self.ip[w]
            v=li.pop()
            if len(li) ==0:
                del self.ip[w]
                self.recycle.add(w)
        else:
            li = self.c[w]
            v=li.pop()
            del self.c[w]
            if len(li) ==0:
                self.recycle.add(w)
            else:
                self.ip[w] = li
        return v
                
            
        

    def popAtStack(self, idx: int) -> int:
        
        p=-1 if idx not in self.ip else idx
        c=-1 if idx not in self.c else idx
        w = max(p,c)
        if w == -1: return w
        v=-1
        if w == p:
            li = self.ip[w]
            v=li.pop()
            if len(li) ==0:
                del self.ip[w]
                self.recycle.add(w)
        else:
            li = self.c[w]
            v=li.pop()
            del self.c[w]
            if len(li) ==0:
                self.recycle.add(w)
            else:
                self.ip[w] = li
        return v
        


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)