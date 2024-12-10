def partOne(filePath):
    with open(filePath) as input:
        # split in lines
        lines = input.readlines()
        # split lines at empty line
        lines = [line.strip() for line in lines]
        index = lines.index('')
        pageRules = lines[:index]
        printOrders = [line.split(',') for line in lines[index+1:]]
        afterRules = parsePageRules(pageRules)
        sum = 0
        for printOrder in printOrders:
            printedPages = []
            wrongOrder = False
            for page in printOrder:
                if page in afterRules:
                    for after in afterRules[page]:
                        if after in printedPages:
                            wrongOrder = True
                            break
                if wrongOrder:
                    break
                printedPages.append(page)
            if len(printedPages) == len(printOrder):
                sum += int(printOrder[len(printOrder)//2])
        print(sum)


def parsePageRules(pageRules):
    beforeRules = {}
    afterRules = {}
    for rule in pageRules:
        rule = rule.split('|')
        before = rule[0]
        after = rule[1]
        if before not in afterRules:
            afterRules[before] = []
        afterRules[before].append(after)
    return afterRules


def partTwo(filePath):
    with open(filePath) as input:
        # split in lines
        lines = input.readlines()
        # split lines at empty line
        lines = [line.strip() for line in lines]
        index = lines.index('')
        pageRules = lines[:index]
        printOrders = [line.split(',') for line in lines[index+1:]]
        afterRules = parsePageRules(pageRules)
        incorrectOrders = filterIncorrectOrders(printOrders, afterRules)
        # sort incorrect orders according to the page rules
        for order in incorrectOrders:
            brokenRules = getBrokenRules(order, afterRules)
            while len(brokenRules) > 0:
                for (page, after) in brokenRules:
                    # switch page and after in order
                    indexPage = order.index(page)
                    indexAfter = order.index(after)
                    order[indexPage] = after
                    order[indexAfter] = page
                brokenRules = getBrokenRules(order, afterRules)
        sum = 0
        for order in incorrectOrders:
            sum += int(order[len(order)//2])
        print(sum)


def filterIncorrectOrders(orders, afterRules):
    incorrectOrders = []
    for printOrder in orders:
        printedPages = []
        wrongOrder = False
        for page in printOrder:
            if page in afterRules:
                for after in afterRules[page]:
                    if after in printedPages:
                        wrongOrder = True
                        break
            printedPages.append(page)
        if wrongOrder:
            incorrectOrders.append(printOrder)
    return incorrectOrders


def getBrokenRules(printOrder, afterRules):
    printedPages = []
    brokenRules = []
    for page in printOrder:
        if page in afterRules:
            for after in afterRules[page]:
                if after in printedPages:
                    brokenRules.append((page, after))
        printedPages.append(page)
    return brokenRules


if __name__ == '__main__':
    #partOne('./aocDay05/example.txt')
    #partOne('./aocDay05/input.txt')
    #partTwo('./aocDay05/example.txt')
    partTwo('./aocDay05/input.txt')