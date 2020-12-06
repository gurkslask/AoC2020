from math import ceil, floor
with open('input.txt') as f:
    data = f.readlines()
    data = [i.replace('\n', '') for i in data]


def main():
    print(parse(data[0]))
    test = "FBFBBFFRLR"
    testrow, testcol = parse(test)
    row = binsearch(testrow, 0, 127)
    col = binsearch(testcol, 0, 7)
    print(row*8+col)
    testlist = ["BFFFBBFRRR",
                "FBFBBFFRLR",
                "FFFBBBFRRR",
                "BBFFBBFRLL"]
    testreslist = []
    for i in testlist:
        row, col = parse(i)
        testreslist.append(binsearch(row, 0, 127) * 8 + binsearch(col, 0, 7))

    print(max(testreslist))

    # Simple done
    reslist = []
    for i in data:
        row, col = parse(i)
        reslist.append(binsearch(row, 0, 127) * 8 + binsearch(col, 0, 7))
    print("Result: ", max(reslist))

    #Advanced
    print(type(reslist))
    reslist.sort()
    for k, v in enumerate(reslist):
        if v - 1 != reslist[k-1]:
            print(v-1)

    pass


def parse(s):
    return s[0:7], s[7:10]

def binsearch(li, mi, ma):
    minn, maxx, = mi, ma
    for k, i in enumerate(li):
        if i in ["F", "L"]:
            maxx = maxx - floor((maxx - minn) / 2)
        if i in ["B", "R"]:
            minn = ceil((maxx - minn) / 2) + minn
        if k == len(li) - 1:
            if "F": return minn
            else: return maxx





if __name__ == '__main__':
    main()
