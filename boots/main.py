import re


def main(data):
    pass


def getdata():
    with open('input.txt') as f:
        data = f.readlines()
        data = [i.replace('\n', '') for i in data]
    return data


if __name__ == '__main__':
    data = getdata()
