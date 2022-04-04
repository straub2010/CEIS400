# File for the class definition for the Inventory object
# B Ross d

class Inventory:
    def __init__(self, itemName, inOut, assignTo, clearanceLevel, serialNumber):
        self.itemName = itemName
        self.inOut = inOut
        self.assignTo = assignTo
        self.clearanceLevel = clearanceLevel
        self.serialNumber = serialNumber

