def partOne(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        lines = [line.strip() for line in lines]
        sum = 0
        for equation in lines:
            result = int(equation.split(':')[0])
            factors = [int(x) for x in equation.split(':')[1].split(' ') if x != '']
            for i in range(0, len(factors) - 1):
                if calc(result, factors, i):
                    sum += result
                    break
        print(sum)


def calc(result, factors, startIndex):
    for j in range(0 if startIndex == 0 else 1, len(factors)):
        # multiply j times starting from startIndex, additions before and after
        tmpRes = factors[0]
        calcString = str(factors[0])
        for k in range(0, len(factors) - 1):
            if k >= startIndex and k < startIndex + j:
                tmpRes *= factors[k + 1]
                calcString += ' * ' + str(factors[k + 1])
            else:
                tmpRes += factors[k + 1]
                calcString += ' + ' + str(factors[k + 1])
        # print debug vis
        if result == 7290:
            print(result, '=', '(', calcString, ')', '=', tmpRes, startIndex, j)
        if tmpRes == result:
            return True
    return False


def partTwo(filePath):
    with open(filePath) as input:
        pass


if __name__ == '__main__':
    partOne('./aocDay07/examplePartOne.txt')
    partOne('./aocDay07/input.txt')
    #partTwo('./aocDay07/examplePartTwo.txt')
    #partTwo('./aocDay07/input.txt')