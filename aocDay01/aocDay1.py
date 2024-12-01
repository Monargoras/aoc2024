def partOne(filePath):
    with open(filePath) as input:
        # split in lines
        lines = input.readlines()
        # split each line at spaces
        lines = [line.split() for line in lines]
        # get first of each line
        leftList = [line[0] for line in lines]
        # get second of each line
        rightList = [line[1] for line in lines]
        # sort the lists
        leftList.sort()
        rightList.sort()
        # get sum of difference between each pair of numbers
        sum = 0
        for i in range(len(leftList)):
            sum += abs(int(rightList[i]) - int(leftList[i]))
        print(sum)


def partTwo(filePath):
    with open(filePath) as input:
        # split in lines
        lines = input.readlines()
        # split each line at spaces
        lines = [line.split() for line in lines]
        # get first of each line
        leftList = [line[0] for line in lines]
        # get second of each line
        rightList = [line[1] for line in lines]
        # get sum of difference between each pair of numbers
        similarityScore = 0
        for i in range(len(leftList)):
            value = int(leftList[i]) * rightList.count(leftList[i])
            similarityScore += value
        print(similarityScore)


if __name__ == '__main__':
    #partOne('./aocDay01/examplePartOne.txt')
    #partOne('./aocDay01/input.txt')
    #partTwo('./aocDay01/examplePartTwo.txt')
    partTwo('./aocDay01/input.txt')