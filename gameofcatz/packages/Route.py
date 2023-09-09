class Route:
    def __init__(self, route, cost):
        self.route = route
        self.cost = cost

    def __str__(self):
        return f'{self.route} - {self.cost}'

    def getRoute(self):
        return self.route

    def getCost(self):
        return self.cost
