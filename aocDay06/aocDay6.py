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
        map = [list(x.strip()) for x in map]
        # find guard position (^) with x and y coordinates
        coordinates = next((x, y) for y, row in enumerate(map) for x, char in enumerate(row) if char == '^')
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        direction = 0
        x, y = coordinates
        listOfRelevantObstructions = []
        while True:
            map[y][x] = 'X'
            if y <= 0 or y >= len(map) - 1 or x <= 0 or x >= len(map[y]) - 1:
                break
            nextX = x + directions[direction][0]
            nextY = y + directions[direction][1]
            while map[nextY][nextX] == '#':
                listOfRelevantObstructions.append((nextX, nextY))
                direction = (direction + 1) % 4
                nextX = x + directions[direction][0]
                nextY = y + directions[direction][1]
            x += directions[direction][0]
            y += directions[direction][1]


if __name__ == '__main__':
    #partOne('./aocDay06/examplePartOne.txt')
    #partOne('./aocDay06/input.txt')
    partTwo('./aocDay06/examplePartTwo.txt')
    #partTwo('./aocDay06/input.txt')