import numpy as np

def partOne(filePath):
    with open(filePath) as input:
        map = input.readlines()
        map = [list(x.strip()) for x in map]
        # create numpy array
        map = np.array(map)
        labels = np.zeros_like(map, dtype=int)
        currentLabel = 0
        equivalences = {}
        letters = set()
        for y in range(len(map)):
            for x in range(len(map[y])):
                letters.add(map[y, x])
                neighbors = []
                if y > 0 and map[y, x] == map[y-1, x] and labels[y-1, x] > 0:
                    neighbors.append(labels[y-1, x])  # Top neighbor
                if x > 0 and map[y, x] == map[y, x-1] and labels[y, x-1] > 0:
                    neighbors.append(labels[y, x-1])  # Left neighbor

                if not neighbors:
                    currentLabel += 1
                    labels[y, x] = currentLabel
                else:
                    minLabel = min(neighbors)
                    labels[y, x] = minLabel
                    for label in neighbors:
                        if label != minLabel:
                            equivalences.setdefault(label, set()).add(minLabel)
        labelMap = {}
        for label in range(1, currentLabel + 1):
            root = label
            while root in equivalences and min(equivalences[root]) != root:
                root = min(equivalences[root])
            labelMap[label] = root
        for y in range(len(map)):
            for x in range(len(map[y])):
                labels[y, x] = labelMap[labels[y, x]]
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        sum = 0
        print(labels)
        for label in range(1, currentLabel + 1):
            coords = np.argwhere(labels == label)
            if len(coords) == 0:
                continue
            outsideBorders = 0
            for coord in coords:
                for direction in directions:
                    neighbor = coord + direction
                    if neighbor[0] < 0 or neighbor[0] >= len(labels) or neighbor[1] < 0 or neighbor[1] >= len(labels[0]) or labels[neighbor[0], neighbor[1]] != label:
                        outsideBorders += 1
            #print(f'Label {label}: {len(coords)} cells, {outsideBorders} outside borders, price {outsideBorders * len(coords)}')
            sum += outsideBorders * len(coords)
        print(sum)


def partTwo(filePath):
    with open(filePath) as input:
        map = input.readlines()
        map = [list(x.strip()) for x in map]
        # create numpy array
        map = np.array(map)
        labels = np.zeros_like(map, dtype=int)
        currentLabel = 0
        equivalences = {}
        letters = set()
        for y in range(len(map)):
            for x in range(len(map[y])):
                letters.add(map[y, x])
                neighbors = []
                if y > 0 and map[y, x] == map[y-1, x] and labels[y-1, x] > 0:
                    neighbors.append(labels[y-1, x])  # Top neighbor
                if x > 0 and map[y, x] == map[y, x-1] and labels[y, x-1] > 0:
                    neighbors.append(labels[y, x-1])  # Left neighbor

                if not neighbors:
                    currentLabel += 1
                    labels[y, x] = currentLabel
                else:
                    minLabel = min(neighbors)
                    labels[y, x] = minLabel
                    for label in neighbors:
                        if label != minLabel:
                            equivalences.setdefault(label, set()).add(minLabel)
        labelMap = {}
        for label in range(1, currentLabel + 1):
            root = label
            while root in equivalences and min(equivalences[root]) != root:
                root = min(equivalences[root])
            labelMap[label] = root
        for y in range(len(map)):
            for x in range(len(map[y])):
                labels[y, x] = labelMap[labels[y, x]]
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        sum = 0
        print(labels)
        for label in range(1, currentLabel + 1):
            coords = np.argwhere(labels == label)
            if len(coords) == 0:
                continue
            outsideBorders = 0
            for coord in coords:
                for direction in directions:
                    neighbor = coord + direction
                    if neighbor[0] < 0 or neighbor[0] >= len(labels) or neighbor[1] < 0 or neighbor[1] >= len(labels[0]) or labels[neighbor[0], neighbor[1]] != label and isCorner(coords, coord):
                        outsideBorders += 1
            #print(f'Label {label}: {len(coords)} cells, {outsideBorders} outside borders, price {outsideBorders * len(coords)}')
            sum += outsideBorders * len(coords)
        print(sum)


def isCorner(coords, point):
    notCorner = [
        ((0, -1), (0, 1)),
        ((-1, 0), (1, 0)),
    ]
    for corner in notCorner:
        if (point[0] + corner[0][0], point[1] + corner[0][1]) in coords and (point[0] + corner[1][0], point[1] + corner[1][1]) in coords:
            print(point, (point[0] + corner[0][0], point[1] + corner[0][1]), (point[0] + corner[1][0], point[1] + corner[1][1]), coords)
            return True
    return False


if __name__ == '__main__':
    #partOne('./aocDay12/example.txt')
    #partOne('./aocDay12/example2.txt')
    #partOne('./aocDay12/example3.txt')
    #partOne('./aocDay12/input.txt')
    partTwo('./aocDay12/example.txt')
    #partTwo('./aocDay12/example2.txt')
    #partTwo('./aocDay12/input.txt')