def partOne(filePath):
    with open(filePath) as input:
        map = input.readlines()
        map = [list(x.strip()) for x in map]
        zeroCoords = [(x, y) for y in range(len(map)) for x in range(len(map[y])) if map[y][x] == '0']
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        sum = 0
        for start in zeroCoords:
            visitedNines = set()
            queue = [(start, 0)]
            while queue:
                (x, y), dist = queue.pop(0)
                if map[y][x] == '9':
                    visitedNines.add((x, y))
                for dx, dy in directions:
                    if 0 <= x + dx < len(map[0]) and 0 <= y + dy < len(map) and int(map[y + dy][x + dx]) == dist + 1:
                        queue.append(((x + dx, y + dy), dist + 1))
            sum += len(visitedNines)
        print(sum)


def partTwo(filePath):
    with open(filePath) as input:
        map = input.readlines()
        map = [list(x.strip()) for x in map]
        zeroCoords = [(x, y) for y in range(len(map)) for x in range(len(map[y])) if map[y][x] == '0']
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        sum = 0
        for start in zeroCoords:
            visitedNines = set()
            queue = [(start, 0, [start])]
            while queue:
                (x, y), dist, path = queue.pop(0)
                if map[y][x] == '9':
                    visitedNines.add((x, y, tuple(tuple(x) for x in path)))
                else:
                    for dx, dy in directions:
                        if 0 <= x + dx < len(map[0]) and 0 <= y + dy < len(map) and int(map[y + dy][x + dx]) == dist + 1:
                            queue.append(((x + dx, y + dy), dist + 1, path + [(x + dx, y + dy)]))
            sum += len(visitedNines)
        print(sum)


if __name__ == '__main__':
    #partOne('./aocDay10/example.txt')
    #partOne('./aocDay10/input.txt')
    #partTwo('./aocDay10/example.txt')
    partTwo('./aocDay10/input.txt')