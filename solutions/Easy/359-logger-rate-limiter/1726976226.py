class Logger:

    def __init__(self):
        self.d = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        good = message not in self.d or (timestamp - self.d[message] >= 10)
        if good:
            self.d[message] = timestamp
        return good
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)