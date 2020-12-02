import re
from operator import xor


def main():
    with open('input.txt') as f:
        data = f.readlines()
        data = [i.replace('\n', '') for i in data]

    testdata=[
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc"
    ]

    # first
    pattern = '^(\d*)-(\d*) (\w): (\w*)'
    count = 0
    for row in data:
        # 0 = min, 1 = max, 2=char, 3 = string
        r = re.match(pattern, row).groups()
        print(r)
        c = r[3].count(r[2])
        if int(r[1]) >= c & c >= int(r[0]):
            count += 1
    print(count)


    print("test")
    count = 0
    for row in testdata:
        # 0 = min, 1 = max, 2=char, 3 = string
        r = re.match(pattern, row).groups()
        print(r)
        c = r[3].count(r[2])
        if int(r[1]) >= c & c >= int(r[0]):
            count += 1
            print("true")
        else:
            print("false")
    print(count)

    # second
    print("test second")
    count = 0
    for row in testdata:
        # 0 = min, 1 = max, 2=char, 3 = string
        r = re.match(pattern, row).groups()
        print(r)
        minn = int(r[0])
        maxx = int(r[1])
        c = r[3].count(r[2])
        if xor(r[3][minn-1] == r[2], r[3][maxx-1] == r[2] ):
            count += 1
            print("true")
        else:
            print("false")
    print(count)

    print("real second")
    count = 0
    for row in data:
        # 0 = min, 1 = max, 2=char, 3 = string
        r = re.match(pattern, row).groups()
        print(r)
        minn = int(r[0])
        maxx = int(r[1])
        c = r[3].count(r[2])
        if xor(r[3][minn-1] == r[2], r[3][maxx-1] == r[2] ):
            count += 1
            print("true")
        else:
            print("false")
    print(count)
if __name__ == '__main__':
    main()
