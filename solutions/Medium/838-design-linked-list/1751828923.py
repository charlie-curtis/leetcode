class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def get(self, index: int) -> int:
        if self.n <= index:
            return -1
        t = self.head
        while index:
            index-=1
            t = t.next
        return t.val

    def connect(self,first, middle, last):
        if first:
            first.next = middle
        if middle:
            middle.prev = first
            middle.next = last
        if last:
            last.prev = middle
    
    def getNode(self, index):
        t = self.head
        while index:
            index-=1
            t = t.next
        return t

    def addAtHead(self, val: int) -> None:
        print("AddAtHead", val)
        self.n+=1
        if self.head == None:
            self.head = self.tail = Node(val)
            self.sanity()
            return
        # size >= 1
        first = Node(val)
        self.connect(first, self.head, self.head.next)
        self.head = first
        self.sanity()

    def addAtTail(self, val: int) -> None:
        print("AddAtTail", val)
        self.n+=1
        if self.head == None:
            self.head = self.tail = Node(val)
            self.sanity()
            return
        last = Node(val)
        self.connect(self.tail.prev, self.tail, last)
        self.tail = last
        self.sanity()
        

    def addAtIndex(self, index: int, val: int) -> None:
        print("AddAtIndex", index)
        if index == self.n:
            self.addAtTail(val)
            self.sanity()
            return
        if index == 0:
            self.addAtHead(val)
            self.sanity()
            return
        if self.get(index) == -1:
            self.sanity()
            return
        self.sanity()
        b = None
        t = self.head
        self.n+=1
        while index:
            b = t
            t = t.next
            index-=1
        node = Node(val)
        fwd = t
        node.next = fwd
        node.prev = b
        if b:
            b.next = node
        if fwd:
            fwd.prev = node
        if node.next == None:
            self.tail = node
        if node.prev == None:
            self.head = node
        self.sanity()

    def deleteAtIndex(self, index: int) -> None:
        print("DeleteAtIndex", index)
        if self.get(index) == -1:
            return
        if self.n == 1:
            self.head = self.tail = None
        elif index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif index+1 == self.n:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        else:
            t = self.head
            b = None
            while index:
                index-=1
                b = t
                t = t.next
            fwd = t.next

            b.next = fwd
            if not fwd:
                print(self.n, index)
            fwd.prev = b
        self.n-=1

    def count(self, v):
        t = v
        i = 0
        seen = []
        while t:
            seen.append(t.val)
            i+=1
            t = t.next
        print(seen)
        return i

    def sanity(self):
        return
        t = self.count(self.head)
        if t != self.n:
            raise ValueError("WRONG", t, self.n)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)