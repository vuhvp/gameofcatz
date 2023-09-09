import re
import route as Route


def chooseOption():
    print('\nWhich operation do you want to do?')
    print('1. Find')
    print('2. Insert')
    print('3. Update')
    print('4. Delete')
    choice = input('Your choice (Enter to quit): ')
    return choice


def find(graph, label):
    edge = graph.getEdge(label)
    if edge:
        showInfo(edge)
    else:
        print('\nEDGE DOES NOT EXIST')


def insert(graph, data, label):
    edge = graph.getEdge(label)
    if not edge:
        fromLable, toLabel = label.split('/')
        if not graph.hasVertex(fromLable):
            print(f'\nNODE {fromLable} DOES NOT EXIST')
        elif not graph.hasVertex(toLabel):
            print(f'\nNODE {toLabel} DOES NOT EXIST')
        else:
            code = input('Enter code label you want to insert: ')  # enter code for new edge
            ecode = data.getEcode(code)
            if ecode:
                graph.addEdge(fromLable, toLabel, ecode)  # add new edge to graph
                data.addEdge(fromLable, toLabel, code)  # add new edge to file data
            else:
                print('\nCODE DOES NOT EXIST')
    else:
        print('\nEDGE ALREADY EXISTS')


def delete(graph, data, label):
    edge = graph.getEdge(label)
    if edge:
        if not canDelete(label, graph, data):  # check if can delete this edge
            print('\nCANNOT DELETE THIS EDGE LABEL, FAIL TO GENERATE ROUTE')
        else:
            graph.removeEdge(label)  # remove edge from graph
            data.removeEdge(label)  # remove edge from file data
    else:
        print('\nEDGE DOES NOT EXIST')


def update(graph, data, label):
    edge = graph.getEdge(label)
    if edge:
        showInfo(edge)  # show old info before update
        code = input('\nEnter another code label you want to update: ')
        ecode = data.getEcode(code)
        if ecode:
            edge.setValue(ecode)  # update edge to graph
            data.updateEdge(label, code)  # update edge to file data
            print(f'Updated code {code} to edge {label}')
        else:
            print('\nCODE DOES NOT EXIST')
    else:
        print('\nEDGE DOES NOT EXIST')


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
    label = input(f'\nEnter edge label you want to {operation} (formart A/B): ')
    if label:
        matched = re.findall("\w+\/\w+", label)  # check if input is correct format
        if matched:
            return label
        else:
            print('\nPLEASE ENTER VALID LABEL')


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


def canDelete(edgeLabel, graph, data):
    print('Checking...')
    routes = Route.generate(graph, data, False)  # generate all routes without calculating cost
    count = 0
    label = '-'.join(edgeLabel.split('/'))  # convert from A/B to A-B
    # if all of routes contains edge (going to remove) -> cannot delete
    # if there are some routes does not contain edge (going to remove) -> can delete
    for route in routes:
        if label in route.getRoute():
            count += 1
    if count == routes.getCount():
        return False
    return True


def showInfo(edge):
    print('\nEDGE INFORMATION')
    print(f'Label: {edge.getLabel()}')
    print(f'Code: {edge.getValue().getCode()}')
    print(f'Weight: {edge.getValue().getWeight()}')
