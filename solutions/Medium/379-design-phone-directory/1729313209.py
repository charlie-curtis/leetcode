from sortedcontainers import SortedList
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.sl = SortedList([x for x in range(maxNumbers)])
        

    def get(self) -> int:
        if len(self.sl) > 0:
            res = self.sl.pop()
            return res
        return -1

        

    def check(self, number: int) -> bool:
        return number in self.sl
        

    def release(self, number: int) -> None:
        if self.check(number):
            return
        self.sl.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)