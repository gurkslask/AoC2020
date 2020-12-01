def main():
    with open('input.txt') as f:
        data = f.readlines()
    data = [int(i.replace("\n", "")) for i in data]
    # Answer one:
    for i in data:
        for ii in data:
            if i + ii == 2020:
                print("Answer one: " + str(i * ii))
                break


    for i in data:
        for ii in data:
            for iii in data:
                if i + ii + iii == 2020:
                    print("Answer two: " + str(i * ii * iii))
                    break



if __name__ == '__main__':
    print("hello")
    main()
