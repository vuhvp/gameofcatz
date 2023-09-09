import route as Route
from packages.DSAHashEntry import DSAHashEntryState


def chooseOption():
    print('\nWhich operation do you want to do?')
    print('1. Find')
    print('2. Insert')
    print('3. Update')
    print('4. Delete')
    choice = input('Your choice (Enter to quit): ')
    return choice


def find(graph, label):
    vertex = graph.getVertex(label)
    if vertex:
        showInfo(vertex)
    else:
        print('\nNODE DOES NOT EXIST')


def insert(graph, data, label):
    vertex = graph.getVertex(label)
    if not vertex:
        code = input('Enter code label you want to insert: ')
        ncode = data.getNcode(code)
        if ncode:
            graph.addVertex(label, ncode)  # add new node to graph
            data.addNode(label, code)   # add new node to file data
        else:
            print('\nCODE DOES NOT EXIST')
    else:
        print('\nNODE ALREADY EXISTS')


def delete(graph, data, label):
    vertex = graph.getVertex(label)
    if vertex:
        if label == data.getStart():
            print('\nCANNOT DELETE START LABEL')
        elif label == data.getEnd():
            print('\nCANNOT DELETE TARGET LABEL')
        elif not canDelete(label, graph, data):
            print('\nCANNOT DELETE THIS LABEL, FAIL TO GENERATE ROUTE')
        else:
            graph.removeVertex(label)  # remove node from graph
            data.removeNode(label)  # remove node from file data
            for edge in data.getEdges():
                if edge.getState() == DSAHashEntryState.USED and label in edge.getKey():
                    data.removeEdge(edge.getKey())  # also remove edge from file data cause there is no more node

    else:
        print('\nNODE DOES NOT EXIST')


def update(graph, data, label):
    vertex = graph.getVertex(label)
    if vertex:
        showInfo(vertex)  # show old info before update
        code = input('\nEnter another code label you want to update: ')
        ncode = data.getNcode(code)
        if ncode:
            vertex.setValue(ncode)  # update node to graph
            data.updateNode(label, code)  # update node to file data
            print(f'Updated code {code} to node {label}')
        else:
            print('\nCODE DOES NOT EXIST')
    else:
        print('\nNODE DOES NOT EXIST')


def enterLabel(option):
    if option == '1':
        operation = 'find'
    elif option == '2':
        operation = 'insert'
    elif option == '3':
        operation = 'update'
    elif option == '4':
        operation = 'delete'
    else:
        return option

    label = input(f'\nEnter node label you want to {operation}: ')
    return label


def operation(graph, data):
    option = chooseOption()
    while option:
        label = enterLabel(option)
        if label:
            if option == '1':
                find(graph, label)
            elif option == '2':
                insert(graph, data, label)
            elif option == '3':
                update(graph, data, label)
            elif option == '4':
                delete(graph, data, label)
            else:
                print('\nINVALID OPTION')
        option = chooseOption()


def canDelete(label, graph, data):
    print('Checking...')
    routes = Route.generate(graph, data, False)  # generate all routes without calculating cost
    count = 0
    # if all of routes contains node (going to remove) -> cannot delete
    # if there are some routes does not contain node (going to remove) -> can delete
    for route in routes:
        if label in route.getRoute():
            count += 1
    if count == routes.getCount():
        return False
    return True


def showInfo(node):
    print('\nNODE INFORMATION')
    print(f'Label: {node.getLabel()}')
    print(f'Code: {node.getValue().getCode()}')
    print(f'Weight: {node.getValue().getWeight()}')
