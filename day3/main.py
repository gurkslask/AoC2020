def main():
    with open('input.txt') as f:
        data = f.readlines()
        data = [i.replace("\n", '') for i in data]

    print(data)

    testdata = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#"]

    # simple
    print("Test: ", slopecheck(testdata, 3, 1))
    print("Real: ", slopecheck(data, 3, 1))

    test = slopecheck(testdata, 1, 1) * slopecheck(testdata, 3, 1) *\
           slopecheck(testdata, 5, 1) * slopecheck(testdata, 7, 1) *\
           slopecheck(testdata, 1, 2)
    print(f"test advanced: {test}")
    res = slopecheck(data, 1, 1) * slopecheck(data, 3, 1) *\
           slopecheck(data, 5, 1) * slopecheck(data, 7, 1) *\
           slopecheck(data, 1, 2)
    print(f" advanced: {res}")

def slopecheck(data, stepx, stepy):
    x = 0
    y = 0
    count = 0
    for row in data:
        x += stepx
        x = x % len(data[0])
        y += stepy
        if y < len(data):
            if data[y][x] == "#":
                count += 1
    return count





if __name__ == '__main__':
    # test 7, real 282
    main()
