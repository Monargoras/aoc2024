def partOne(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        lines = [line.strip() for line in lines]
        sum = 0
        resultFactorTuples = [(int(equation.split(':')[0]), [int(x) for x in equation.split(':')[1].split(' ') if x != '']) for equation in lines]
        for (result, factors) in resultFactorTuples:
            if calcOne(result, factors):
                sum += result
        print(sum)


def calcOne(result, values, current=None):
    if current is None:
        current = values[0]
        values = values[1:]
    
    if not values:
        return current == result
    
    next_value = values[0]
    remaining_values = values[1:]

    # addition
    if calcOne(result, remaining_values, current + next_value):
        return True

    # multiplication
    if calcOne(result, remaining_values, current * next_value):
        return True

    return False


def partTwo(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        lines = [line.strip() for line in lines]
        sum = 0
        resultFactorTuples = [(int(equation.split(':')[0]), [int(x) for x in equation.split(':')[1].split(' ') if x != '']) for equation in lines]
        for (result, factors) in resultFactorTuples:
            if calcTwo(result, factors):
                sum += result
        print(sum)


def calcTwo(result, values, current=None):
    if current is None:
        current = values[0]
        values = values[1:]
    
    if not values:
        return current == result
    
    next_value = values[0]
    remaining_values = values[1:]

    # addition
    if calcTwo(result, remaining_values, current + next_value):
        return True

    # multiplication
    if calcTwo(result, remaining_values, current * next_value):
        return True
    
    # concatenation
    if calcTwo(result, remaining_values, int(str(current) + str(next_value))):
        return True

    return False


if __name__ == '__main__':
    #partOne('./aocDay07/example.txt')
    #partOne('./aocDay07/input.txt')
    #partTwo('./aocDay07/example.txt')
    partTwo('./aocDay07/input.txt')