from packages.DSAHashEntry import DSAHashEntryState


def chooseOption():
    print('\nWhich operation do you want to do?')
    print('1. Node code operation')
    print('2. Edge code operation')
    choice = input('Your choice (Enter to quit): ')
    return choice


def codeOperation():
    print('\nWhich operation do you want to do?')
    print('1. Insert')
    print('2. Update')
    print('3. Delete')
    choice = input('Your choice (Enter to quit): ')
    return choice


def enterLabel(option):
    if option == '1':
        operation = 'insert'
    elif option == '2':
        operation = 'update'
    elif option == '3':
        operation = 'delete'
    else:
        return option

    label = input(f'\nEnter code label you want to {operation}: ')
    return label


def operation(data, graph):
    option = chooseOption()
    while option:
        if option == '1' or option == '2':  # choose node code operation or edge code operation
            listCode(data, option)
            operation = codeOperation()  # display menu operation for both node and edge
            while operation:
                label = enterLabel(operation)
                if label:
                    if operation == '1':
                        insert(data, option, label)
                    elif operation == '2':
                        update(data, graph, option, label)
                    elif operation == '3':
                        delete(data, graph, option, label)
                    else:
                        print('\nINVALID OPERATION')
                listCode(data, option)
                operation = codeOperation()
        else:
            print('\nINVALID OPTION')
        option = chooseOption()


def listCode(data, option):
    print('\nLIST OF CODE')
    rowFormat = '{:<10}\t{:<10}\t{:<6}'
    print(rowFormat.format('Code', 'Description', 'Weight'))

    if option == '1':
        ncodes = data.getNcodes()
        for code in ncodes:
            if code.getState() == DSAHashEntryState.USED:  # only get USED state
                if code.getValue().getCode() == '-':  # display No impact if code is minus '-'
                    des = 'No impact'
                else:
                    if code.getValue().getDescription():
                        des = code.getValue().getDescription()
                    else:
                        des = ''
                print(rowFormat.format(code.getValue().getCode(), des, code.getValue().getWeight()))
    else:
        ecodes = data.getEcodes()
        for code in ecodes:
            if code.getState() == DSAHashEntryState.USED:  # only get USED state
                if code.getValue().getCode() == '-':  # display No impact if code is minus '-'
                    des = '1 unit'
                else:
                    if code.getValue().getDescription():
                        des = code.getValue().getDescription()
                    else:
                        des = code.getValue().getCode() + ' units'
                print(rowFormat.format(code.getValue().getCode(), des, code.getValue().getWeight()))


def insert(data, option, label):
    code = getCode(data, label, option)
    if not code:
        try:
            weight = int(input('Enter weight: '))  # enter weight for new code
            des = input('Enter description: ')  # enter description for new code
            if weight and des:
                if option == '1':
                    data.addNcode(label, weight, des)
                    print(f'Added code ({label},{weight})')
                else:
                    if weight >= 0:  # weight of edge code cannot be negative
                        data.addEcode(label, weight, des)
                        print(f'Added code ({label},{weight})')
                    else:
                        print('\nEDGE WEIGHT CANNOT BE NEGATIVE OR ZERO')
        except:
            print('\nINVALID VALUE, NUMBER ONLY')
    else:
        print('\nCODE ALREADY EXIST')


def update(data, graph, option, label):
    code = getCode(data, label, option)
    if code:
        try:
            print('\nCODE INFORMATION')
            print(f'Label: {code.getCode()}')
            print(f'Weight: {code.getWeight()}')
            weight = int(input('\nEnter new weight: '))
            if option == '1':
                if weight:
                    code.setWeight(weight)
                    print(f'Updated code {label} with weight {weight}')
                    updateGraphNode(graph, code)  # update value of node in graph to new code weight
            else:
                if weight != None:
                    if weight > 0:
                        code.setWeight(weight)
                        print(f'Updated code {label} with weight {weight}')
                        updateGraphEdge(graph, code)  # update value of edge in graph to new code weight
                    else:
                        print('\nEDGE WEIGHT CANNOT BE NEGATIVE OR ZERO')
        except:
            print('INVALID VALUE, NUMBER ONLY')
    else:
        print('\nCODE DOES NOT EXIST')


def delete(data, graph, option, label):
    code = getCode(data, label, option)
    if code:
        if label == '-':
            print('\nCANNOT DELETE THIS CODE')
        elif option == '1':
            data.removeNcode(label)
            updateNcode(data, graph, code)  # update node code in graph to code minus
        else:
            data.removeEcode(label)
            updateEcode(data, graph, code)  # update node code in graph to code minus
    else:
        print('\nCODE DOES NOT EXIST')


def getCode(data, label, option):
    if option == '1':
        code = data.getNcode(label)
    else:
        code = data.getEcode(label)
    return code


def updateGraphNode(graph, code):
    for vertex in graph.getVertices():
        if vertex.getValue().getCode() == code.getCode():
            vertex.setValue(code)


def updateGraphEdge(graph, code):
    for edge in graph.edges:
        if edge.getValue().getCode() == code.getCode():
            edge.setValue(code)


def updateNcode(data, graph, code):
    minus = data.getNcode('-')
    for vertex in graph.getVertices():
        if vertex.getValue().getCode() == code.getCode():
            vertex.setValue(minus)
    for node in data.getNodes():
        if node.getState() == DSAHashEntryState.USED and node.getValue().getCode() == code.getCode():
            node.getValue().setCode('-')


def updateEcode(data, graph, code):
    minus = data.getNcode('-')
    for edge in graph.edges:
        if edge.getValue().getCode() == code.getCode():
            edge.setValue(minus)
    for edge in data.getEdges():
        if edge.getState() == DSAHashEntryState.USED and edge.getValue().getCode() == code.getCode():
            edge.getValue().setCode('-')
