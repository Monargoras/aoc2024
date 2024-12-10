import re


def partOne(filePath):
    with open(filePath) as input:
        txt = input.read()
        regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
        matches = re.findall(regex, txt)
        sum = 0
        for match in matches:
            sum += int(match[0]) * int(match[1])
        print(sum)



def partTwo(filePath):
    with open(filePath) as input:
        txt = input.read()
        regexMult = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
        regexDo = re.compile(r'do\(\)')
        regexDont = re.compile(r'don\'t\(\)')
        matchesMult = re.finditer(regexMult, txt)
        matchesDo = re.finditer(regexDo, txt)
        matchesDoObject = [{'start': match.start(), 'end': match.end()} for match in matchesDo]
        matchesDont = re.finditer(regexDont, txt)
        matchesDontObject = [{'start': match.start(), 'end': match.end()} for match in matchesDont]
        sum = 0
        for match in matchesMult:
            if isSafeMatch(match, matchesDontObject, matchesDoObject):
                sum += int(match.group(1)) * int(match.group(2))
        print(sum)


def isSafeMatch(match, matchesDontObject, matchesDoObject):
    closestDontStart = -1
    closestDoStart = -1
    for dont in matchesDontObject:
        if dont['start'] < match.start() and dont['start'] > closestDontStart:
            closestDontStart = dont['start']
    for do in matchesDoObject:
        if do['start'] < match.start() and do['start'] > closestDoStart:
            closestDoStart = do['start']
    return closestDontStart == -1 or closestDoStart > closestDontStart


if __name__ == '__main__':
    #partOne('./aocDay03/example.txt')
    #partOne('./aocDay03/input.txt')
    #partTwo('./aocDay03/example.txt')
    partTwo('./aocDay03/input.txt')