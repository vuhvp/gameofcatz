import sys
import code as Code
import display as Display
import edge as Edge
import export as Export
import file as File
import graph as Graph
import network as Network
import node as Node
import route as Route


def usage():
    print('\nPlease input mode to run this program')
    print('\tinput -i for interactive mode')
    print('\tinput -s for simulation mode\n')


def interactive_menu():
    print('\nINTERACTIVE MENU')
    print('1. Load input file')
    print('2. Node operations')
    print('3. Edge operations')
    print('4. Parameter tweaks')
    print('5. Display graph')
    print('6. Display world')
    print('7. Generate routes')
    print('8. Display routes')
    print('9. Save network')
    print('10. Visualize')
    choice = input('Your choice (Enter to quit): ')
    return choice


def simulate(inputFile, outputFile):
    print('\nLoad input file')
    data = File.load(inputFile)
    print('\nCreate graph')
    graph = Graph.create(data)
    print('\nGenerate routes')
    routes = Route.generate(graph, data, True)
    rows = Route.generateRows(routes)
    print('\nExport to output file')
    Export.toCSV(rows, outputFile)


def main():
    if len(sys.argv) < 2:
        usage()
    else:
        mode = sys.argv[1]
        if mode == '-i':
            graph = None
            data = None
            routes = None
            choice = interactive_menu()
            while choice:
                if choice == '1':
                    filename = input('\nEnter input file name: ')
                    while not filename:
                        filename = input('Enter input file name: ')
                    data = File.load(filename)
                    if data:
                        print('\nCREATE GRAPH\n')
                        graph = Graph.create(data)
                elif choice == '2':
                    if graph:
                        print('\nNODE OPERATION')
                        Node.operation(graph, data)
                    else:
                        print('\nPLEASE LOAD INPUT FILE FIRST')
                elif choice == '3':
                    if graph:
                        print('\nEDGE OPERATION')
                        Edge.operation(graph, data)
                    else:
                        print('\nPLEASE LOAD INPUT FILE FIRST')
                elif choice == '4':
                    if graph:
                        print('\nCODE OPERATION')
                        Code.operation(data, graph)
                    else:
                        print('\nPLEASE LOAD INPUT FILE FIRST')
                elif choice == '5':
                    if graph:
                        print('\nWEIGHTED ADJACENCY MATRIX\n')
                        matrix = graph.getWeightedMatrix()
                        Display.displayMatrix(matrix)
                        ask = input('\nDo you want to export this matrix? (Y/N): ').lower()
                        if ask == 'y' or ask == 'yes':
                            Export.toCSV(matrix)
                            print('Exported')
                    else:
                        print('\nPLEASE LOAD INPUT FILE FIRST')
                elif choice == '6':
                    if graph:
                        print('\nDISPLAY WORLD\n')
                        world = Graph.generateWorld(data, graph)
                        Display.displayWorld(world)
                        ask = input('\nDo you want to export this world? (Y/N): ').lower()
                        if ask == 'y' or ask == 'yes':
                            Export.toCSV(world)
                            print('Exported')

                    else:
                        print('\nPLEASE LOAD INPUT FILE FIRST')
                elif choice == '7':
                    if graph:
                        print('\nGENERATE POSSIBLE ROUTES')
                        routes = Route.generate(graph, data, True)
                        print('Generated')
                    else:
                        print('\nPLEASE LOAD INPUT FILE FIRST')
                elif choice == '8':
                    if graph:
                        if routes:
                            print('\nPOSSIBLE ROUTES WITH RANKING\n')
                            rows = Route.generateRows(routes)
                            Display.displayRoutes(rows)
                            ask = input('\nDo you want to export these routes? (Y/N): ').lower()
                            if ask == 'y' or ask == 'yes':
                                Export.toCSV(rows)
                                print('Exported')
                        else:
                            print('\nPLEASE GENERATE ROUTES FIRST')
                    else:
                        print('\nPLEASE LOAD INPUT FILE FIRST')
                elif choice == '9':
                    if data:
                        network = Network.generate(data)
                        Export.toText(network)
                        print('Exported')
                    else:
                        print('\nPLEASE LOAD INPUT FILE FIRST')
                elif choice == '10':
                    if data:
                        graph.visualize()
                    else:
                        print('\nPLEASE LOAD INPUT FILE FIRST')
                else:
                    print('\nINVALID OPTION')
                choice = interactive_menu()
        elif mode == '-s':
            if len(sys.argv) < 4:
                print('Please enter the name for input and output file!')
            else:
                inputFile = sys.argv[2]
                outputFile = sys.argv[3]
                simulate(inputFile, outputFile)


if __name__ == '__main__':
    main()
