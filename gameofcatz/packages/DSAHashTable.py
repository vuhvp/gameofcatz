# Source code obtained from Huynh Van Phi Vu, Practical 7

import numpy as np
from packages.DSAHashEntry import DSAHashEntry, DSAHashEntryState


class DSAHashTable:
    def __init__(self, capacity, isResized=False):
        tableCapacity = self._nextPrime(capacity)
        print(f'The next prime number of {capacity} is {tableCapacity}!')
        if isResized:
            print(f'Resize hash table from capacity {tableCapacity}!\n')
        else:
            print(f'Create hash table from capacity {tableCapacity}!\n')
        self.hashArray = np.array([DSAHashEntry() for _ in range(tableCapacity)])
        self.count = 0

    def put(self, key, value, isResized=False):
        if self._find(key) > -1:
            raise ValueError(f'Key {key} already exists!')
        elif self.getCount() == self._getCapacity():
            print('\nThe hash table has reached its maximum size, resizing hash table with double capacity!')
            print(f'Double capacity: {self._getCapacity()} x 2 = {self._getCapacity() * 2}')
            self._resize()
            self.put(key, value)
        else:
            hashIdx = self._hash(key)
            entry = DSAHashEntry(key, value, DSAHashEntryState.USED)

            if self.hashArray[hashIdx].getState() == DSAHashEntryState.FREE:
                self.hashArray[hashIdx] = entry
            else:
                step = self._stepHash(hashIdx)
                probeIdx = hashIdx + step
                isFree = False
                while not isFree:
                    probeIdx = probeIdx % self._getCapacity()
                    if self.hashArray[probeIdx].getState() == DSAHashEntryState.FREE:
                        self.hashArray[probeIdx] = entry
                        isFree = True
                    else:
                        probeIdx += step
            self.count += 1
            if not isResized:
                print(f'Added entry {key} to hash table!')

    def get(self, key):
        hashIdx = self._find(key)
        if hashIdx > -1:
            return self.hashArray[hashIdx].getValue()

    def update(self, key, value):
        hashIdx = self._find(key)
        if hashIdx > -1:
            self.hashArray[hashIdx].setValue(value)
            print(f'Updated entry {self.hashArray[hashIdx].getKey()} from hash table!')
        else:
            raise ValueError(f'Key {key} does not exist!')

    def remove(self, key):
        hashIdx = self._find(key)
        if hashIdx > -1:
            oldEntry = self.hashArray[hashIdx]
            entry = DSAHashEntry(None, None, DSAHashEntryState.PREVIOUSLY_USED)
            self.hashArray[hashIdx] = entry
            print(f'Removed entry {oldEntry.getKey()} from hash table!')
            self.count -= 1
        else:
            raise ValueError(f'Key {key} does not exist!')

    def getLoadFactor(self):
        return self.getCount() / self._getCapacity()

    def getCount(self):
        return self.count

    def _resize(self):
        hashArray = self.hashArray.copy()
        self.__init__(self._getCapacity() * 2, True)
        for item in hashArray:
            self.put(item.getKey(), item.getValue(), True)

    def _hash(self, key):
        hashIdx = 0
        for i in range(len(key)):
            hashIdx = (31 * hashIdx) + ord(key[i])
        return hashIdx % self._getCapacity()

    def _stepHash(self, key):
        maxStep = self._nextPrime((self._getCapacity() - 1) / 2)
        hashStep = maxStep - (key % maxStep)
        return hashStep

    def _nextPrime(self, capacity):
        if capacity % 2 == 0:
            prime = capacity - 1
        else:
            prime = capacity
        isPrime = False
        while not isPrime:
            prime = prime + 2
            isPrime = True
            count = 3
            while count ** 2 <= prime and isPrime:
                if prime % count == 0:
                    isPrime = False
                else:
                    count = count + 2
        return int(prime)

    def _find(self, key):
        hashIdx = self._hash(key)
        origIdx = hashIdx
        step = self._stepHash(hashIdx)
        isContinued = True
        keyFound = -1
        while isContinued:
            state = self.hashArray[hashIdx].getState()
            if state == DSAHashEntryState.FREE:
                isContinued = False
            else:
                if self.hashArray[hashIdx].getKey() == key:
                    keyFound = hashIdx
                    isContinued = False
                else:
                    hashIdx = (hashIdx + step) % self._getCapacity()
                    if hashIdx == origIdx:
                        isContinued = False
        return keyFound

    def _getCapacity(self):
        return self.hashArray.size
