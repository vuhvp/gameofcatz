# Source code obtained from Huynh Van Phi Vu, Practical 4

class DSAListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getNext(self):
        return self.next

    def setNext(self, value):
        self.next = value

    def getPrev(self):
        return self.prev

    def setPrev(self, value):
        self.prev = value
