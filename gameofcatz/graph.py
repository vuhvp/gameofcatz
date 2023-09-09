from packages.DSAGraph import DSAGraph
from packages.DSAHashEntry import DSAHashEntryState
from packages.DSALinkedList import DSALinkedList


def create(data):
    graph = DSAGraph()
    nodes = data.getNodes()  # get nodes data from file
    edges = data.getEdges()  # get edges data from file
    for node in nodes:
        if node.getState() == DSAHashEntryState.USED:
            code = data.getNcode(node.getValue().getCode())
            graph.addVertex(node.getValue().getLabel(), code)
    for edge in edges:
        if edge.getState() == DSAHashEntryState.USED:
            code = data.getEcode(edge.getValue().getCode())
            graph.addEdge(edge.getValue().getFrom(), edge.getValue().getTo(), code)
    return graph


def generateWorld(data, graph):
    world = DSALinkedList()
    for ncode in data.getNcodes():
        item = DSALinkedList()  # item acts as 1 row
        count = 0
        if ncode.getState() == DSAHashEntryState.USED:
            code = ncode.getValue().getCode()
            nodeList = DSALinkedList()  # collect all nodes that have corresponding code
            for v in graph.getVertices():
                if v.getValue().getCode() == code:
                    count += 1  # count how many node that corresponding code
                    nodeList.insertLast(v.getLabel())
            # generate 1 row
            nodes = ','.join(label for label in nodeList)
            if code == '-':
                item.insertLast('No impact (-)')
            else:
                if ncode.getValue().getDescription():
                    item.insertLast(ncode.getValue().getDescription())
                else:
                    item.insertLast(ncode.getValue().getCode())
            item.insertLast(count)
            item.insertLast('\"' + nodes + '\"')
            # add row to world
            # a row looks like this: nodetype, count, list of node
            world.insertFirst(item)

    # generate header row
    header = DSALinkedList()
    header.insertLast('Type')
    header.insertLast('Count')
    header.insertLast('Node')
    world.insertFirst(header)
    return world
