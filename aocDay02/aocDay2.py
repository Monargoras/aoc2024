def partOne(filePath):
    with open(filePath) as input:
        # split in lines
        lines = input.readlines()
        # split each line at spaces
        lines = [[int(level) for level in line.split()] for line in lines]
        safeReports = 0
        for line in lines:
            # guard if report only has one level
            if len(line) == 1:
                safeReports += 1
                continue
            prevLevel = line[0]
            decreasing = prevLevel - line[1] > 0
            safeReport = True
            for level in line[1:]:
                if (decreasing and prevLevel < level) or (not decreasing and prevLevel > level) or abs(prevLevel-level) > 3 or abs(prevLevel-level) < 1:
                    safeReport = False
                    break
                prevLevel = level
            if safeReport:
                safeReports += 1
        print(safeReports)



def partTwo(filePath):
    with open(filePath) as input:
        # split in lines
        lines = input.readlines()
        # split each line at spaces
        lines = [[int(level) for level in line.split()] for line in lines]
        safeReports = 0
        for line in lines:
            safeReport = checkReport(line)
            if safeReport:
                safeReports += 1
        print(safeReports)


def checkReport(report, recursive = False):
    # guard if report only has one level
    if len(report) == 1:
        return True
    prevLevel = report[0]
    decreasing = prevLevel - report[-1] > 0
    safeReport = True
    index = 0
    for level in report[1:]:
        if (decreasing and prevLevel < level) or (not decreasing and prevLevel > level) or abs(prevLevel-level) > 3 or abs(prevLevel-level) < 1:
            if recursive:
                return False
            return checkReport(report[0:index] + report[index+1:], True) or checkReport(report[0:index+1] + report[index+2:], True)
        prevLevel = level
        index += 1
    return safeReport

if __name__ == '__main__':
    #partOne('./aocDay02/examplePartOne.txt')
    #partOne('./aocDay02/input.txt')
    #partTwo('./aocDay02/examplePartTwo.txt')
    partTwo('./aocDay02/input.txt')