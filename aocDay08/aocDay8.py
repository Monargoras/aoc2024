def partOne(filePath):
    with open(filePath) as input:
        map = input.readlines()
        map = [list(x.strip()) for x in map]
        antennaMap = {}
        for y, row in enumerate(map):
            for x, char in enumerate(row):
                if char != '.':
                    if antennaMap.get(char) == None:
                        antennaMap[char] = []
                    antennaMap[char].append((x, y))
        antinodeSet = set()
        for coords in antennaMap.values():
            # iterate every pair of coords
            for i in range(len(coords)):
                for j in range(i+1, len(coords)):
                    x1, y1 = coords[i]
                    x2, y2 = coords[j]
                    antinodeLocations = []
                    xDiff = x1 - x2
                    yDiff = y1 - y2
                    if x1 + xDiff in range(0, len(map[y])) and y1 + yDiff in range(0, len(map)):
                        antinodeLocations.append((x1 + xDiff, y1 + yDiff))
                    if x2 - xDiff in range(0, len(map[y])) and y2 - yDiff in range(0, len(map)):
                        antinodeLocations.append((x2 - xDiff, y2 - yDiff))
                    for antinode in antinodeLocations:
                        antinodeSet.add(antinode)
        print(len(antinodeSet))



def partTwo(filePath):
    with open(filePath) as input:
        map = input.readlines()
        map = [list(x.strip()) for x in map]
        antennaMap = {}
        for y, row in enumerate(map):
            for x, char in enumerate(row):
                if char != '.':
                    if antennaMap.get(char) == None:
                        antennaMap[char] = []
                    antennaMap[char].append((x, y))
        antinodeSet = set()
        for coords in antennaMap.values():
            # iterate every pair of coords
            for i in range(len(coords)):
                for j in range(i+1, len(coords)):
                    x1, y1 = coords[i]
                    x2, y2 = coords[j]
                    antinodeLocations = [(x1, y1), (x2, y2)]
                    xDiff = x1 - x2
                    yDiff = y1 - y2
                    while x1 + xDiff in range(0, len(map[y])) and y1 + yDiff in range(0, len(map)):
                        antinodeLocations.append((x1 + xDiff, y1 + yDiff))
                        x1 += xDiff
                        y1 += yDiff
                    while x2 - xDiff in range(0, len(map[y])) and y2 - yDiff in range(0, len(map)):
                        antinodeLocations.append((x2 - xDiff, y2 - yDiff))
                        x2 -= xDiff
                        y2 -= yDiff
                    for antinode in antinodeLocations:
                        antinodeSet.add(antinode)
        print(len(antinodeSet))


if __name__ == '__main__':
    #partOne('./aocDay08/example.txt')
    #partOne('./aocDay08/input.txt')
    #partTwo('./aocDay08/example.txt')
    partTwo('./aocDay08/input.txt')