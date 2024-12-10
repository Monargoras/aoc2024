def partOne(filePath):
    with open(filePath) as input:
        # split in lines
        lines = input.readlines()
        # split each line at spaces
        lines = [list(line.strip()) for line in lines]
        sum = 0
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == 'X' or lines[y][x] == 'S':
                    sum += checkXmas(lines, y, x, lines[y][x])
        print(sum)


def checkXmas(lines, y, x, startLetter):
    letters = ['X', 'M', 'A', 'S'] if startLetter == 'X' else ['S', 'A', 'M', 'X']
    sum = 0
    # check horizontal
    if len(lines[y]) > x+3 and lines[y][x+1] == letters[1] and lines[y][x+2] == letters[2] and lines[y][x+3] == letters[3]:
        sum += 1
    # check vertical
    if len(lines) > y+3 and lines[y+1][x] == letters[1] and lines[y+2][x] == letters[2] and lines[y+3][x] == letters[3]:
        sum += 1
    # check diagonal
    if len(lines) > y+3 and len(lines[y]) > x+3 and lines[y+1][x+1] == letters[1] and lines[y+2][x+2] == letters[2] and lines[y+3][x+3] == letters[3]:
        sum += 1
    # check other diagonal
    if len(lines) > y+3 and x-3 >= 0 and lines[y+1][x-1] == letters[1] and lines[y+2][x-2] == letters[2] and lines[y+3][x-3] == letters[3]:
        if y == 6 and x == 2:
            print(lines[y][x], lines[y+1][x-1], lines[y+2][x-2], lines[y+3][x-3])
        sum += 1
    return sum


def partTwo(filePath):
    with open(filePath) as input:
        # split in lines
        lines = input.readlines()
        # split each line at spaces
        lines = [list(line.strip()) for line in lines]
        sum = 0
        for y in range(len(lines) - 1):
            for x in range(len(lines[y]) - 1):
                if lines[y][x] == 'A':
                    if checkCrossMas(lines, y, x):
                        sum += 1
        print(sum)


def checkCrossMas(lines, y, x):
    sum = 0
    # check one direction
    if 0 < y < len(lines) - 1 and 0 < x < len(lines[y]) - 1 and lines[y-1][x-1] == 'M' and lines[y+1][x+1] == 'S' or lines[y-1][x-1] == 'S' and lines[y+1][x+1] == 'M':
        sum += 1
    # check other direction
    if 0 < y < len(lines) - 1 and 0 < x < len(lines[y]) - 1 and lines[y-1][x+1] == 'M' and lines[y+1][x-1] == 'S' or lines[y-1][x+1] == 'S' and lines[y+1][x-1] == 'M':
        sum += 1
    return sum > 1


if __name__ == '__main__':
    #partOne('./aocDay04/example.txt')
    #partOne('./aocDay04/input.txt')
    #partTwo('./aocDay04/example.txt')
    partTwo('./aocDay04/input.txt')