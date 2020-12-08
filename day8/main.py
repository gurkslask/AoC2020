import re
from copy import copy, deepcopy


def main(data):
    data = parse(data)
    visited = []
    done = False
    acc = 0
    step = 0
    while not done:
        visited.append(step)
        if data[step][0] == 'nop':
            step += 1
        elif data[step][0] == 'acc':
            acc += data[step][1]
            step += 1
        elif data[step][0] == 'jmp':
            step += data[step][1]
        if step in visited:
            done = True
    return acc


def main2(data):
    dataorg = parse(data)
    for k, v in enumerate(dataorg):
        data = deepcopy(dataorg)
        acc = 0
        step = 0
        done = False
        rerun = False
        visited = []
        if data[k][0] == 'jmp':
            data[k][0] = 'nop'
        elif data[k][0] == 'nop':
            data[k][0] = 'jmp'

        while not (done or rerun):
            visited.append(step)
            if data[step][0] == 'nop':
                step += 1
            elif data[step][0] == 'acc':
                acc += data[step][1]
                step += 1
            elif data[step][0] == 'jmp':
                step += data[step][1]
            if step in visited:
                rerun = True
            if step > len(data) - 1:
                done = True
        if done:
            break
    return acc


def parse(s: str):
    s = [i.split(' ') for i in s]
    s = [[i[0], int(i[1])] for i in s]
    return s

def getdata(path):
    with open(path) as f:
        data = f.readlines()
        data = [i.replace('\n', '') for i in data]
    return data


if __name__ == '__main__':
    data = getdata('input.txt')
    testdata = getdata('testinput.txt')
    print("Test: ", main(testdata))
    print("Real: ", main(data))
    print("Part 2 test: ", main2(testdata))
    print("Part 2 real: ", main2(data))
