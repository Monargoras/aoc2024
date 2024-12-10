def partOne(filePath):
    with open(filePath) as input:
        line = input.readline()
        numbers = [int(f) for f in list(line.strip())]
        uncomepressedDisk = []
        fileId = 0
        for i in range(0, len(numbers)):
            if i % 2 == 0:
                uncomepressedDisk.extend([fileId] * numbers[i])
                fileId += 1
            else:
                uncomepressedDisk.extend(['.'] * numbers[i])
        for i in reversed(range(0, len(uncomepressedDisk))):
            if uncomepressedDisk[i] != '.':
                leftMostDotIndex = getLeftMostDotIndex(uncomepressedDisk)
                if leftMostDotIndex != -1 and leftMostDotIndex < i:
                    uncomepressedDisk[leftMostDotIndex] = uncomepressedDisk[i]
                    uncomepressedDisk[i] = '.'
        sum = 0
        for i in range(0, len(uncomepressedDisk)):
            if uncomepressedDisk[i] != '.':
                sum += i * uncomepressedDisk[i]
            else:
                break
        print(sum)


def getLeftMostDotIndex(uncomepressedDisk):
    for i in range(0, len(uncomepressedDisk)):
        if uncomepressedDisk[i] == '.':
            return i
    return -1


def partTwo(filePath):
    with open(filePath) as input:
        line = input.readline()
        numbers = [int(f) for f in list(line.strip())]
        uncomepressedDisk = []
        fileId = 0
        for i in range(0, len(numbers)):
            if i % 2 == 0:
                uncomepressedDisk.extend([fileId] * numbers[i])
                fileId += 1
            else:
                uncomepressedDisk.extend(['.'] * numbers[i])
        for i in reversed(range(0, len(uncomepressedDisk))):
            if uncomepressedDisk[i] != '.':
                fileSize = uncomepressedDisk.count(uncomepressedDisk[i])
                leftMostDotIndex = getLeftMostDotIndexOfSize(uncomepressedDisk, fileSize)
                if leftMostDotIndex != -1 and leftMostDotIndex < i:
                    for j in range(0, fileSize):
                        uncomepressedDisk[leftMostDotIndex + j] = uncomepressedDisk[i - j]
                        uncomepressedDisk[i - j] = '.'
                    i -= fileSize
        sum = 0
        for i in range(0, len(uncomepressedDisk)):
            if uncomepressedDisk[i] != '.':
                sum += i * uncomepressedDisk[i]
        print(sum)


def getLeftMostDotIndexOfSize(uncomepressedDisk, size):
    for i in range(0, len(uncomepressedDisk)):
        if i + size <= len(uncomepressedDisk) and all(uncomepressedDisk[j] == '.' for j in range(i, i + size)):
            return i
    return -1


if __name__ == '__main__':
    #partOne('./aocDay09/example.txt')
    #partOne('./aocDay09/input.txt')
    #partTwo('./aocDay09/example.txt')
    partTwo('./aocDay09/input.txt')