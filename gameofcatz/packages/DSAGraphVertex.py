# Source code obtained from Huynh Van Phi Vu, Practical 6

from packages.DSALinkedList import DSALinkedList


class DSAGraphVertex:
    def __init__(self, label, value):
        self.label = label
        self.value = value
        self.links = DSALinkedList()
        self.visited = False

    def __str__(self):
        return f'{self.label}'

    def getLabel(self):
        return self.label

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getAdjacent(self):
        return self.links

    def hasAdjacent(self, label):
        for vertex in self.links:
            if vertex.getLabel() == label:
                return True
        return False

    def addEdge(self, vertex):
        self.links.insertLast(vertex)

    def setVisited(self):
        self.visited = True

    def clearVisited(self):
        self.visited = False

    def getVisited(self):
        return self.visited
