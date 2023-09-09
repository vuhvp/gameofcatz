import re
from packages.Route import Route
from packages.DSALinkedList import DSALinkedList
from packages.DSAStack import DSAStack


class RouteList:
    def __init__(self, graph, data):
        self.routes = DSALinkedList()
        self.stack = DSAStack()
        self.graph = graph
        self.data = data
        self.start = data.getStart()
        self.end = data.getEnd()

    def getRoutes(self):
        return self.routes

    def generate(self, withCost):
        self.withCost = withCost
        startVertex = self.graph.getVertex(self.start)
        self.stack.push(startVertex)
        self._findRoute(startVertex)
        self.stack.pop()

    def _findRoute(self, startVertex):
        adjacencyList = startVertex.getAdjacent()
        for desVertex in adjacencyList:
            if desVertex.getLabel() == self.end:  # reach the target, no need to go furthur
                self.stack.push(desVertex)
                route = self._createRoute()
                self.routes.insertFirst(route)
                self.stack.pop()  # pop out when finish generating route
            elif not self.stack.hasValue(desVertex):
                self.stack.push(desVertex)
                self._findRoute(desVertex)
                self.stack.pop()  # pop current vertex out of stack after checking all adjacency list

    def _createRoute(self):
        cost, route, path = 0, '', ''
        for vertex in self.stack:
            if not route:  # add first label to route
                route += vertex.getLabel()
            else:
                route = vertex.getLabel() + '-' + route  # add next label to route
            if self.withCost:
                cost += vertex.getValue().getWeight()
                if not path:  # add first label to path
                    path += vertex.getLabel()
                else:
                    path = vertex.getLabel() + '/' + path  # add next label to path
                matched = re.findall("\w+\/\w+", path)
                if matched:
                    edge = self.data.getEdge(path)
                    code = self.data.getEcode(edge.getCode())
                    cost += code.getWeight()
                    path = path.split('/')[0]
        r = Route(route, cost)
        return r
