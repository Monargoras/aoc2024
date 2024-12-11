from functools import cache


def partOne(filePath):
    with open(filePath) as input:
        # split in lines
        line = input.readline()
        # split each line at spaces
        stones = [int(stone) for stone in line.split()]
        for i in range(25):
            stones = blink(stones)
        print(len(stones))


def blink(stones):
    newStoneMap = []
    for i in range(len(stones)):
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0:
            first, second = int(str(stones[i])[:len(str(stones[i]))//2]), int(str(stones[i])[len(str(stones[i]))//2:])
            stones[i] = first
            newStoneMap.append((second, i+1))
        else:
            stones[i] = stones[i] * 2024
    for i in range(len(newStoneMap)):
        stones.insert(newStoneMap[i][1] + i, newStoneMap[i][0])
    return stones


def partTwo(filePath):
    with open(filePath) as input:
        # split in lines
        line = input.readline()
        # split each line at spaces
        stones = [int(stone) for stone in line.split()]
        stones = sum(countStones(stone, 75) for stone in stones)
        print(stones)


def blinkSingleStone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        first, second = int(str(stone)[:len(str(stone))//2]), int(str(stone)[len(str(stone))//2:])
        return [first, second]
    else:
        return [stone * 2024]
    return stones


@cache
def countStones(stone, iterationsLeft):
    if iterationsLeft == 0:
        return 1
    return sum(countStones(s, iterationsLeft - 1) for s in blinkSingleStone(stone))


if __name__ == '__main__':
    #partOne('./aocDay11/example.txt')
    #partOne('./aocDay11/input.txt')
    #partTwo('./aocDay11/example.txt')
    partTwo('./aocDay11/input.txt')