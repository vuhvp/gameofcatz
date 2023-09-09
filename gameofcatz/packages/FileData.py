from packages.DSAHashTable import DSAHashTable


class CodeInfo:
    def __init__(self, code, weight, description):
        self.code = code
        self.weight = weight
        self.description = description

    def getCode(self):
        return self.code

    def getWeight(self):
        return self.weight

    def getDescription(self):
        return self.description

    def setWeight(self, value):
        self.weight = value

    def setDescription(self, value):
        self.description = value


class NodeInfo:
    def __init__(self, label, code):
        self.label = label
        self.code = code

    def getLabel(self):
        return self.label

    def getCode(self):
        return self.code

    def setCode(self, code):
        self.code = code


class EdgeInfo:
    def __init__(self, fromLabel, toLabel, code):
        self.fromLabel = fromLabel
        self.toLabel = toLabel
        self.code = code

    def getFrom(self):
        return self.fromLabel

    def getTo(self):
        return self.toLabel

    def getCode(self):
        return self.code

    def setCode(self, code):
        self.code = code


class FileData:
    def __init__(self):
        self.ncodes = DSAHashTable(10)
        self.nodes = DSAHashTable(50)
        self.ecodes = DSAHashTable(10)
        self.edges = DSAHashTable(100)
        self.start = None
        self.end = None

    def addNcode(self, code, weight, description=None):
        ncode = CodeInfo(code, weight, description)
        self.ncodes.put(code, ncode)

    def addNode(self, label, code):
        node = NodeInfo(label, code)
        self.nodes.put(label, node)

    def addEcode(self, code, weight, description=None):
        ecode = CodeInfo(code, weight, description)
        self.ecodes.put(code, ecode)

    def addEdge(self, fromLabel, toLabel, code):
        edge = EdgeInfo(fromLabel, toLabel, code)
        self.edges.put(f'{fromLabel}/{toLabel}', edge)

    def removeNcode(self, code):
        self.ncodes.remove(code)

    def removeEcode(self, code):
        self.ecodes.remove(code)

    def removeNode(self, label):
        self.nodes.remove(label)

    def removeEdge(self, label):
        self.edges.remove(label)

    def updateNode(self, label, code):
        node = NodeInfo(label, code)
        self.nodes.update(label, node)

    def updateEdge(self, label, code):
        fromLabel, toLabel = label.split('/')
        edge = EdgeInfo(fromLabel, toLabel, code)
        self.edges.update(label, edge)

    def getNcodes(self):
        return self.ncodes.hashArray

    def getNodes(self):
        return self.nodes.hashArray

    def getEcodes(self):
        return self.ecodes.hashArray

    def getEdges(self):
        return self.edges.hashArray

    def getNcode(self, code):
        return self.ncodes.get(code)

    def getNode(self, code):
        return self.nodes.get(code)

    def getEcode(self, code):
        return self.ecodes.get(code)

    def getEdge(self, code):
        return self.edges.get(code)

    def setStart(self, label):
        self.start = label

    def setEnd(self, label):
        self.end = label

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def getNcodeCount(self):
        return self.ncodes.getCount()

    def getNodeCount(self):
        return self.nodes.getCount()

    def getEcodeCount(self):
        return self.ecodes.getCount()

    def getEdgeCount(self):
        return self.edges.getCount()
