def partOne(filePath):
    with open(filePath) as input:
        map = input.readlines()
        map = [list(x.strip()) for x in map]
        # find guard position (^) with x and y coordinates
        coordinates = next((x, y) for y, row in enumerate(map) for x, char in enumerate(row) if char == '^')
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        direction = 0
        x, y = coordinates
        while True:
            map[y][x] = 'X'
            if y <= 0 or y >= len(map) - 1 or x <= 0 or x >= len(map[y]) - 1:
                break
            nextX = x + directions[direction][0]
            nextY = y + directions[direction][1]
            while map[nextY][nextX] == '#':
                direction = (direction + 1) % 4
                nextX = x + directions[direction][0]
                nextY = y + directions[direction][1]
            x += directions[direction][0]
            y += directions[direction][1]
        xCount = sum(row.count('X') for row in map)
        print(xCount)


def partTwo(filePath):
    with open(filePath) as input:
        map = input.readlines()
        origMap = [list(x.strip()) for x in map]
        map = [list(x.strip()) for x in map]
        # find guard position (^) with x and y coordinates
        coordinates = next((x, y) for y, row in enumerate(map) for x, char in enumerate(row) if char == '^')
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        direction = 0
        x, y = coordinates
        while True:
            map[y][x] = 'X'
            if y <= 0 or y >= len(map) - 1 or x <= 0 or x >= len(map[y]) - 1:
                break
            nextX = x + directions[direction][0]
            nextY = y + directions[direction][1]
            while map[nextY][nextX] == '#':
                direction = (direction + 1) % 4
                nextX = x + directions[direction][0]
                nextY = y + directions[direction][1]
            x += directions[direction][0]
            y += directions[direction][1]
        # exclude starting position
        xCoords = [(x, y) for y, row in enumerate(map) for x, char in enumerate(row) if char == 'X' and (x, y) != coordinates]
        # reset map
        map = origMap
        # add obstruction as 'O' to the map one X position at a time and test if its a loop
        sum = 0
        for i in range(len(xCoords)):
            x, y = xCoords[i]
            map[y][x] = '#'
            print(f'x: {x}, y: {y}, sum: {sum}, progress: {i}/{len(xCoords)}')
            if isLoop(map, coordinates):
                sum += 1
            map[y][x] = '.'
        print(sum)


def isLoop(map, start):
    coordinates = start
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction = 0
    x, y = coordinates
    visitedCoords = []
    while True:
        map[y][x] = 'X'
        # get last two items in list
        if len(visitedCoords) > 1:
            newTuple = [visitedCoords[-1], (x, y)]
            if sublist(newTuple, visitedCoords):
                return True
        # tuple of last and current position
        visitedCoords.append((x, y))
        if y <= 0 or y >= len(map) - 1 or x <= 0 or x >= len(map[y]) - 1:
            break
        nextX = x + directions[direction][0]
        nextY = y + directions[direction][1]
        while map[nextY][nextX] == '#':
            direction = (direction + 1) % 4
            nextX = x + directions[direction][0]
            nextY = y + directions[direction][1]
        x += directions[direction][0]
        y += directions[direction][1]
    return False


def sublist(sublist, mainList):
    # Iterate over the main list and check for the sublist
    for i in range(len(mainList) - 1):
        if mainList[i:i+2] == sublist:
            return True
    return False


if __name__ == '__main__':
    #partOne('./aocDay06/example.txt')
    #partOne('./aocDay06/input.txt')
    #partTwo('./aocDay06/example.txt')
    partTwo('./aocDay06/input.txt')