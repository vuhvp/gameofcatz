# Source code obtained from Huynh Van Phi Vu, Practical 7

from enum import Enum


class DSAHashEntryState(Enum):
    FREE = 1
    USED = 2
    PREVIOUSLY_USED = 3


class DSAHashEntry:
    def __init__(self, key=None, value=None, state=DSAHashEntryState.FREE):
        self.key = key
        self.value = value
        self.state = state

    def __str__(self):
        return (self.key, self.value, self.state)

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state
