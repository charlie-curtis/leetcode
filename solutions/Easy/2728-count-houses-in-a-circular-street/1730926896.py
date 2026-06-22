# Definition for a street.
# class Street:
#     def openDoor(self):
#         pass
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
#     def moveLeft(self):
#         pass
class Solution:
    def houseCount(self, street: Optional['Street'], k: int) -> int:


        for i in range(k):
            if street.isDoorOpen():
                street.closeDoor()
            street.moveLeft()
        
        street.openDoor()
        street.moveLeft()
        for i in range(k):
            if street.isDoorOpen():
                return i+1
            street.moveLeft()

        