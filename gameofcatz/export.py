def toCSV(rows, filename=None):
    while not filename:
        filename = input('Enter output file name: ')
    with open(f'{filename}.csv', 'w') as f:
        for row in rows:
            line = ','.join(str(col) for col in row) + '\n'
            f.write(line)


def toText(rows):
    filename = input('\nEnter output file name: ')
    while not filename:
        filename = input('Enter output file name: ')
    with open(f'{filename}.txt', 'w') as f:
        for row in rows:
            f.write(row + '\n')
