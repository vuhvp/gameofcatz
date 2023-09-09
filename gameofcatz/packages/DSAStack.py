# Source code obtained from Huynh Van Phi Vu, Practical 4

from packages.DSAListNode import DSAListNode


class DSAStack:
    def __init__(self):
        self.front = None
        self.count = 0

    def __iter__(self):
        self._cur = self.front
        return self

    def __next__(self):
        curval = None
        if not self._cur:
            raise StopIteration
        else:
            curval = self._cur.getValue()
            self._cur = self._cur.getNext()
        return curval

    def isEmpty(self):
        return self.front == None

    def push(self, value):
        newNode = DSAListNode(value)
        if self.isEmpty():
            self.front = newNode
        else:
            newNode.setNext(self.front)
            self.front = newNode
        self.count += 1

    def pop(self):
        removedValue = None
        if self.isEmpty():
            raise Exception('Stack is empty, cannot pop!')
        elif not self.front.getNext():
            removedValue = self.top()
            self.front = None
        else:
            removedValue = self.top()
            self.front = self.front.getNext()
        self.count -= 1
        return removedValue

    def top(self):
        if self.isEmpty():
            raise Exception('Stack is empty, cannot get top value!')
        else:
            return self.front.getValue()

    def hasValue(self, value):
        currNode = self.front
        while currNode:
            if currNode.getValue() == value:
                return True
            currNode = currNode.getNext()
        return False

    def getCount(self):
        return self.count
