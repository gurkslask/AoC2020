import re


def main(data):
    # Part 1
    count = 0
    pdata = parse(data)
    for group in pdata:
        ss = set()
        for dude in group:
            s = set(i for i in dude)
            ss = ss.union(s)
        count += len(ss)
    print("Part 1: ", count)

    # Part 2
    count = 0
    for group in pdata:
        ss = set(i for i in group[0])
        for dude in group:
            s = set(i for i in dude)
            ss.intersection_update(s)
        count += len(ss)
    print("Part 2: ", count)
    pass


def parse(data):
    plist = []
    tlist = []
    for row in data:
        if row == '':
            plist.append(tlist)
            tlist = []
        else:
            tlist.append(row)
    return plist


def getdata():
    with open('input.txt') as f:
        data = f.readlines()
        data = [i.replace('\n', '') for i in data]
    return data


if __name__ == '__main__':
    data = getdata()
    main(data)
