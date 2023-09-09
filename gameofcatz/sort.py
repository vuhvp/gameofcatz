# Source code obtained from Java By Patel, https://javabypatel.blogspot.com/2015/12/merge-sort-linked-list.html

from packages.DSAListNode import DSAListNode


def mergeSort(startNode):
    if not startNode or not startNode.getNext():
        return startNode

    middle = _getMiddle(startNode)
    nextOfMiddle = middle.getNext()
    middle.setNext(None)
    left = mergeSort(startNode)
    right = mergeSort(nextOfMiddle)
    sortedList = _mergeTwoList(left, right)
    return sortedList


def _mergeTwoList(leftStart, rightStart):
    merged = None
    temp = None
    lastAddedNode = DSAListNode(None)
    while leftStart and rightStart:
        if leftStart.getValue().getCost() > rightStart.getValue().getCost():
            temp = rightStart
            rightStart = rightStart.getNext()
        else:
            temp = leftStart
            leftStart = leftStart.getNext()
        if not merged:
            merged = temp
        else:
            lastAddedNode.setNext(temp)
        lastAddedNode = temp

    if leftStart:
        lastAddedNode.setNext(leftStart)
    else:
        lastAddedNode.setNext(rightStart)
    return merged


def _getMiddle(startNode):
    if not startNode:
        return startNode

    pointer1 = startNode
    pointer2 = startNode
    while pointer2 and pointer2.getNext() and pointer2.getNext().getNext():
        pointer1 = pointer1.getNext()
        pointer2 = pointer2.getNext().getNext()
    return pointer1
