import re


def main2(data):
    rot = 0
    rotations = {
        0: 'N',
        90: 'E',
        180: 'S',
        270: 'W',
    }
    sums = {
        'N': 0,
        'E': 0,
        'S': 0,
        'W': 0,
    }
    waypoint = [10, 1] #  x, y, +x = east, -x = west, +y = north, -y south
    ship = [0, 0]
    def rotfixer(clockwise):
        # 10, 4 -> 4, -10
        if clockwise:
            waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
        elif not clockwise:
            waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]


    for instruction in data:
        if instruction[0] == 'F':
            for times in range(instruction[1]):
                ship[0] += waypoint[0]
                ship[1] += waypoint[1]
                # Move boat according to waypoint x number of times
                if waypoint[0] > 0:
                    sums['E'] += waypoint[0]
                if waypoint[0] < 0:
                    sums['W'] += waypoint[0]

                if waypoint[1] > 0:
                    sums['N'] += waypoint[1]
                if waypoint[1] < 0:
                    sums['S'] += waypoint[1]
                # print(times)
                # print(ship)
        elif instruction[0] == 'R':
            for i in range(int(instruction[1] / 90)):
                rot += 90
                rotfixer(True)
        elif instruction[0] == 'L':
            for i in range(int(instruction[1] / 90)):
                rot -= 90
                rotfixer(False)
        else:
            if instruction[0] == 'N': waypoint[1] += instruction[1]
            if instruction[0] == 'S': waypoint[1] -= instruction[1]
            if instruction[0] == 'E': waypoint[0] += instruction[1]
            if instruction[0] == 'W': waypoint[0] -= instruction[1]
        # print(waypoint)
    print(sums)
    return (abs(ship[0]) + abs(ship[1]))

def main(data):
    rot = 90
    north = 0  # south = - numbers
    east = 0  # west = - numbers
    rotations = {
        0: 'N',
        90: 'E',
        180: 'S',
        270: 'W',
    }
    sums = {
        'N': 0,
        'E': 0,
        'S': 0,
        'W': 0,
    }
    for instruction in data:
        if instruction[0] == 'F':
            sums[rotations[rot % 360]] += instruction[1]
        elif instruction[0] == 'R':
            rot += instruction[1]
        elif instruction[0] == 'L':
            rot -= instruction[1]
        else:
            sums[instruction[0]] += instruction[1]
    return (abs(sums['N'] - sums['S']) + abs(sums['W'] - sums['E']))


def getdata(path):
    with open(path) as f:
        data = f.readlines()
        data = [i.replace('\n', '') for i in data]
        data = [(i[0], int(i[1:])) for  i in data]
    return data


if __name__ == '__main__':
    data = getdata('input.txt')
    testdata = getdata('testinput.txt')
    # print("Test: ", main(testdata))
    # print("Real: ", main(data))
    print("Test: ", main2(testdata))
    print("Real: ", main2(data))
