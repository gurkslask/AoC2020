import re
from collections import defaultdict
from itertools import combinations
from copy import deepcopy


def main(data):
    memory = defaultdict(int)
    restr = r'mem\[(\d*)\] = (\d*)'
    for inst in data:
        if 'mask' in inst:
            mask = inst.split('=')[1].strip()
        if 'mem' in inst:
            m = re.search(restr, inst)
            bnum = [i for i in bin(int(m[2]))[2:].zfill(36)]
            for k, v in enumerate(mask[::-1]):
                print(bnum)
                if v != 'X':
                    print(k)
                    bnum[len(bnum) - 1 - k] = v
            memory[m[1]] = int("0b" + ''.join(bnum), 2)

    summ = 0 
    for i in memory:
        summ += memory[i]
    return summ

def main2(data):
    memory = defaultdict(int)
    restr = r'mem\[(\d*)\] = (\d*)'
    for inst in data:
        if 'mask' in inst:
            mask = inst.split('=')[1].strip()
        if 'mem' in inst:
            m = re.search(restr, inst)
            bnum = [i for i in bin(int(m[1]))[2:].zfill(36)]
            # print("Aregf: ", ''.join(bnum))
            # print("Mask:  ", mask)
            for k, v in enumerate(mask[::-1]):
                if v == '0':
                    continue
                elif v == '1':
                    bnum[len(bnum) - 1 - k] = '1'
                elif v == 'X':
                    bnum[len(bnum) - 1 - k] = 'X'

            nollettlist = []
            xcount = bnum.count('X')
            for i in range(xcount):
                nollettlist.append(1)
                nollettlist.append(0)
            combs = combinations(nollettlist, xcount)
            addresses = set()
            bnum_c = deepcopy(bnum)
            for comb in combs:
                index = 0
                for num in comb:
                    index = bnum.index('X', index)
                    bnum_c[index] = str( num )
                    index += 1
                addresses.add(int(''.join(bnum_c), 2))
            # print(addresses)
            for address in addresses:
                memory[address] = int( m[2] )

    summ = 0
    for i in memory:
        summ += memory[i]
    return summ




def getdata(path):
    with open(path) as f:
        data = f.readlines()
        data = [i.replace('\n', '') for i in data]
    return data


if __name__ == '__main__':
    data = getdata('input.txt')
    testdata = getdata('testinput.txt')
    testdata2 = getdata('testinput2.txt')
    # print("Test: ", main(testdata))
    # print("Real: ", main(data))
    print("Test: ", main2(testdata2))
    print("Real: ", main2(data))
