import re
from queue import Queue
from collections import defaultdict


def main(data):
    # part 1
    bagDict = parse(data)
    bag_q = Queue()
    bag_q.put('shiny gold')
    colors_set = set()
    def bagChecker(wanted):
        for bag, values in bagDict.items():
            # print(values.values())
            for _, color in values:
                if color == wanted:
                    bag_q.put(bag)
                    colors_set.add(bag)
    while bag_q.empty() is False:
        bagChecker(bag_q.get())

    print("part 1: ", len(colors_set))

    '''def checkChildren(d, color):
        summa = 0
        # print("color amount: ", color, amount)
        for values in d[color]:
            try:
                summa += int(values[0])
            except ValueError:
                summa += 1
        # return summa * int(amount)
        return summa
        # summa = sum(d[color].keys())
        # print(summa)


    def checkChildren2(d, color, amount):
        summa = 0
        # print("color amount: ", color, amount)
        for values in d[color]:
            try:
                summa += int(values[0])
            except ValueError:
                summa += 0
        # return summa * int(amount)
        return summa
        # summa = sum(d[color].keys())
        # print(summa)

    summa = 0
    # Take the sum of first bag 
    for values in bagDict["shiny gold"]:
        summa += int(values[0])

    # check children
    for color in bagDict["shiny gold"]:
        summa += checkChildren(bagDict, color[1], color[0])

    summa2 = 0

    def rere(pos):
        print("in rere")
        for values in bagDict[pos]:
            summa = 0
            if values[1] in 'no other':
                pass
            else:
                rere(values[1])
            print("values in rere: ", values)
            nonlocal summa2
            if values[1] in 'no other':
                pass
            else:
                f = int(values[0])
                # summa = checkChildren(bagDict, values[1])
                summa += sum[int(i[0].strip()) for i bagDict[values[1].values()]
                summa2 += (summa * f) 
            print("summa2: ", summa2)
        return
    rere('shiny gold')'''
    q2 = Queue()
    summa = 0
    def rere(wanted):
        nonlocal summa
        if bagDict[wanted][0][1] not in 'no other':
            for t in bagDict[wanted]:
                for _ in range(int(t[0])):
                    q2.put(t[1])
                summa += int(t[0])
    q2.put('shiny gold')
    while q2.empty() is False:
        rere(q2.get())

    # print(summa2)
    print("Part 2 result: ", summa)



def parse(data):
    bagdict = defaultdict(dict)
    for i in data:
        i = i.split(' contain ')
        firstpattern = '^(.*) bag.?'
        secondpattern = r'([0-9] )*(\w* \w*) bag.?[,.]'
        key = re.findall(firstpattern, i[0])
        bagdict[key[0]] = re.findall(secondpattern, i[1])
    return bagdict


def getdata():
    with open('input.txt') as f:
        data = f.readlines()
        data = [i.replace('\n', '') for i in data]
    return data


def gettestdata():
    with open('testdata2.txt') as f:
        data = f.readlines()
        data = [i.replace('\n', '') for i in data]
    return data


if __name__ == '__main__':
    testdata = gettestdata()
    data = getdata()
    print("Test: ", main(testdata))
    print("Real: ", main(data))
