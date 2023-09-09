# Source code obtained from Huynh Van Phi Vu, Practical 6

class DSAGraphEdge:
    def __init__(self, src, des, label, value):
        self.src = src
        self.des = des
        self.label = label
        self.value = value

    def getLabel(self):
        return self.label

    def getValue(self):
        return self.value

    def getFrom(self):
        return self.src

    def getTo(self):
        return self.des

    def setValue(self, value):
        self.value = value
