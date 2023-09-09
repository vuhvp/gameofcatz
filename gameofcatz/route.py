from packages.RouteList import RouteList
from packages.DSALinkedList import DSALinkedList
from timeit import default_timer as timer
from datetime import timedelta
import sort as Sort


def generate(graph, data, withCost):
    routes = RouteList(graph, data)
    startTime = timer()
    routes.generate(withCost)  # generate route with option withCost=True
    endTime = timer()
    # print(timedelta(seconds=endTime-startTime))
    if withCost:  # sort if withCost=True
        sorted = DSALinkedList()
        sorted.head = Sort.mergeSort(routes.getRoutes().head)
        return sorted
    else:
        return routes.routes


def generateRows(routes):
    rows = DSALinkedList()
    header = DSALinkedList()
    header.insertLast('Rank')
    header.insertLast('Cost')
    header.insertLast('Route')
    rows.insertLast(header)  # add header row
    rank = 0
    curCost = 0
    for route in routes:
        row = DSALinkedList()  # create one row
        if route.getCost() > curCost:
            curCost = route.getCost()
            rank += 1
        row.insertLast(rank)
        row.insertLast(route.getCost())
        row.insertLast(route.getRoute())
        rows.insertLast(row)
    return rows
