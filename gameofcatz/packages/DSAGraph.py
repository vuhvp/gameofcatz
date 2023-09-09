# Source code obtained from Huynh Van Phi Vu, Practical 6

from packages.DSALinkedList import DSALinkedList
from packages.DSAGraphVertex import DSAGraphVertex
from packages.DSAGraphEdge import DSAGraphEdge
import matplotlib.pyplot as plt
import networkx as nx


class DSAGraph:
    def __init__(self):
        self.vertices = DSALinkedList()
        self.edges = DSALinkedList()

    def addVertex(self, label, value):
        if not self.hasVertex(label):
            vertex = DSAGraphVertex(label, value)
            self.vertices.insertLast(vertex)
            print(f'Added node {label} to graph')

    def addEdge(self, fromLabel, toLabel, value):
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        if not fromVertex:
            raise ValueError(f'Graph does not have node {fromLabel}!')
        elif not toVertex:
            raise ValueError(f'Graph does not have node {toLabel}!')
        elif fromVertex.hasAdjacent(toLabel):
            raise ValueError(f'Graph already has edge ({fromLabel}/{toLabel})!')
        else:
            fromVertex.addEdge(toVertex)
            edge = DSAGraphEdge(fromVertex, toVertex, f'{fromLabel}/{toLabel}', value)
            self.edges.insertLast(edge)
            print(f'Added edge {fromLabel}/{toLabel} to graph')

    def removeVertex(self, label):
        removedVertex = self.getVertex(label)
        if removedVertex:
            for edge in self.edges:
                edgeLabel = edge.getLabel()
                if label in edgeLabel:
                    self.removeEdge(edgeLabel)
            self.vertices.remove(removedVertex)
            print(f'Removed node {label}')
            return removedVertex
        else:
            raise ValueError(f'Label {label} does not exist!')

    def removeEdge(self, label):
        removedEdge = self.getEdge(label)
        if removedEdge:
            self.edges.remove(removedEdge)
            fromLabel, toLabel = label.split('/')
            fromVertex = self.getVertex(fromLabel)
            toVertex = self.getVertex(toLabel)
            fromVertex.getAdjacent().remove(toVertex)
            print(f'Removed edge label {label}')
            return removedEdge
        else:
            raise ValueError(f'Edge label {label} does not exist!')

    def hasVertex(self, label):
        vertex = self.getVertex(label)
        if vertex:
            return True
        return False

    def getVertex(self, label):
        for vertex in self.vertices:
            if vertex.getLabel() == label:
                return vertex
        return None

    def getEdge(self, label):
        for edge in self.edges:
            if edge.getLabel() == label:
                return edge

    def getVertices(self):
        return self.vertices

    def getEdges(self):
        return self.edges

    def getAdjacent(self, label):
        vertex = self.getVertex(label)
        return vertex.getAdjacent()

    def isAdjacent(self, fromLabel, toLabel):
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        if fromVertex.getAdjacent().hasValue(toVertex):
            return True
        return False

    def getVertexLabels(self):
        labels = DSALinkedList()
        for vertex in self.vertices:
            labels.insertLast(vertex.getLabel())
        labels.sort()
        for label in labels:
            print(label, 'label')
        return labels

    def getWeightedMatrix(self):
        labels = self.getVertexLabels()
        rows = DSALinkedList()
        l1 = labels.head
        while l1:
            line = DSALinkedList()
            line.insertLast(l1.getValue())
            l2 = labels.head
            while l2:
                if self.isAdjacent(l1.getValue(), l2.getValue()):
                    edge = self.getEdge(f'{l1.getValue()}/{l2.getValue()}')
                    line.insertLast(edge.getValue().getWeight())
                else:
                    line.insertLast(0)
                l2 = l2.getNext()
            rows.insertLast(line)
            l1 = l1.getNext()
        labels.insertFirst('')
        rows.insertFirst(labels)
        return rows

    def getVertexCount(self):
        return self.vertices.getCount()

    def getEdgeCount(self):
        return self.edges.getCount()

    def visualize(self):
        # Obtained from Wubin Ding, https://stackoverflow.com/a/47135311
        # Obtained from Francesco Sgaramella, https://stackoverflow.com/a/22862610
        edges = []
        node_labels = dict()
        edge_labels = dict()
        for edge in self.edges:
            fromLable, toLabel = edge.getLabel().split('/')
            edges.append([fromLable, toLabel])
            edge_labels[(fromLable, toLabel)] = edge.getValue().getWeight()
        plt.figure(figsize=(8, 7))
        G = nx.Graph()
        G.add_edges_from(edges)
        pos = nx.spring_layout(G, scale=2)
        for node in G.nodes():
            vertex = self.getVertex(node)
            if vertex.getValue().getCode() == '-':
                node_labels[node] = f'{vertex.getLabel()}\n{vertex.getValue().getWeight()}'
            else:
                node_labels[node] = f'{vertex.getLabel()}\n{vertex.getValue().getCode()}:{vertex.getValue().getWeight()}'
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=10, font_color='#2c77b4')
        nx.draw(G, pos, node_size=1200, font_size=10, labels=node_labels, node_color='#2c77b4', font_color='whitesmoke')
        plt.show()
