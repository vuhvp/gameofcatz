# Source code obtained from Huynh Van Phi Vu, Practical 4

from packages.DSAListNode import DSAListNode


class DSALinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        self._cur = self.head
        return self

    def __next__(self):
        curval = None
        if not self._cur:
            raise StopIteration
        else:
            curval = self._cur.getValue()
            self._cur = self._cur.getNext()
        return curval

    def insertFirst(self, value):
        newNode = DSAListNode(value)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode

    def insertLast(self, value):
        newNode = DSAListNode(value)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.setPrev(self.tail)
            self.tail.setNext(newNode)
            self.tail = newNode

    def removeFirst(self):
        removedValue = None
        if self.isEmpty():
            raise Exception('LinkedList is empty!')
        elif not self.head.getNext():
            removedValue = self.peekFirst()
            self.head = None
            self.tail = None
        else:
            removedValue = self.peekFirst()
            self.head = self.head.getNext()
            self.head.setPrev(None)
        return removedValue

    def removeLast(self):
        removedValue = None
        if self.isEmpty():
            raise Exception('LinkedList is empty!')
        elif not self.head.getNext():
            removedValue = self.peekFirst()
            self.head = None
            self.tail = None
        else:
            removedValue = self.peekLast()
            self.tail = self.tail.getPrev()
            self.tail.setNext(None)
        return removedValue

    def remove(self, value):
        removedValue = None
        if self.isEmpty():
            raise Exception('LinkedList is empty!')
        elif not self.head.getNext():
            self.head = None
            self.tail = None
        elif self.head.getValue() == value:
            self.head = self.head.getNext()
            self.head.setPrev(None)
        elif self.tail.getValue() == value:
            self.tail = self.tail.getPrev()
            self.tail.setNext(None)
        else:
            prevNode = self.head
            currNode = self.head.getNext()
            while currNode:
                if currNode.getValue() == value:
                    removedValue = currNode.getValue()
                    prevNode.setNext(currNode.getNext())
                prevNode = currNode
                currNode = currNode.getNext()
        return removedValue

    def isEmpty(self):
        return self.head == None

    def peekFirst(self):
        if self.isEmpty():
            raise Exception('LinkedList is empty!')
        else:
            return self.head.getValue()

    def peekLast(self):
        if self.isEmpty():
            raise Exception('LinkedList is empty!')
        else:
            return self.tail.getValue()

    def hasValue(self, value):
        currNode = self.head
        while currNode:
            if currNode.getValue() == value:
                return True
            currNode = currNode.getNext()
        return False

    def getCount(self):
        count = 0
        currNode = self.head
        while currNode:
            count += 1
            currNode = currNode.getNext()
        return count

    def sort(self):
        # Source code obtained from Huynh Van Phi Vu, Practical 1
        curNode = self.head
        while curNode:
            minNode = curNode
            nextNode = minNode.getNext()
            while nextNode:
                # Obtained from DelftStack, https://www.delftstack.com/howto/python/user-input-int-python/
                if minNode.getValue().isnumeric():  # need change to int cause it return True for '2' > '10'
                    minValue = int(minNode.getValue())
                    nextValue = int(nextNode.getValue())
                else:
                    minValue = minNode.getValue()
                    nextValue = nextNode.getValue()
                if minValue > nextValue:
                    minNode = nextNode
                nextNode = nextNode.getNext()
            if minNode != curNode:
                tempValue = curNode.getValue()
                curNode.setValue(minNode.getValue())
                minNode.setValue(tempValue)
            curNode = curNode.getNext()
