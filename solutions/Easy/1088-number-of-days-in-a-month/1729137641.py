class Solution:
    def numberOfDays(self, year: int, month: int) -> int:

        days = [31,28, 31, 30, 31,30,31, 31, 30, 31, 30, 31]

        ans = days[month-1]

        isLeapYear = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
        if isLeapYear and month == 2:
            return 29
        return ans