def displayMatrix(rows):
    rowFormat = '{:<3}' * rows.peekFirst().getCount()
    for row in rows:
        print(rowFormat.format(*row))


def displayRoutes(rows):
    rowFormat = '{:<6}{:<10}{:<}'
    for row in rows:
        print(rowFormat.format(*row))


def displayWorld(rows):
    rowFormat = '{:<10}\t{:<6}\t{:<}'
    for row in rows:
        print(rowFormat.format(*row))
