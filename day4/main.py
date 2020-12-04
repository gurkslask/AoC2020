import re


def main():
    with open('input.txt') as f:
        data = f.readlines()
        data = [i.replace('\n', '') for i in data]

    testdata = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
                'byr:1937 iyr:2017 cid:147 hgt:183cm',
                '',
                'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
                'hcl:#cfa07d byr:1929',
                '',
                'hcl:#ae17e1 iyr:2013',
                'eyr:2024',
                'ecl:brn pid:760753108 byr:1931',
                'hgt:179cm',
                '',
                'hcl:#cfa07d eyr:2025 pid:166559648',
                'iyr:2011 ecl:brn hgt:59in',
                '']
    # Simple
    testparsed = parse(testdata)
    testres = check(testparsed)
    print("simple test result: ", testres)

    parsed = parse(data)
    res = check(parsed)
    print("Simple result: ", res)
    advtestdata = ['eyr:1972 cid:100',
                   'hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926',
                   '',
                   'iyr:2019',
                   'hcl:#602927 eyr:1967 hgt:170cm',
                   'ecl:grn pid:012533040 byr:1946',
                   '',
                   'hcl:dab227 iyr:2012',
                   'ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277',
                   '',
                   'hgt:59cm ecl:zzz',
                   'eyr:2038 hcl:74454a iyr:2023',
                   'pid:3556412378 byr:2007',
                   '',
                   'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980',
                   'hcl:#623a2f',
                   '',
                   'eyr:2029 ecl:blu cid:129 byr:1989',
                   'iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',
                   '',
                   'hcl:#888785',
                   'hgt:164cm byr:2001 iyr:2015 cid:88',
                   'pid:545766238 ecl:hzl',
                   'eyr:2022',
                   '',
                   'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719',
                   '']

    testparsed = parse(advtestdata)
    testres = advancedcheck(testparsed)
    print("Advanced test result: ", testres)

    parsed = parse(data)
    advres = advancedcheck(parsed)
    print("Advanced result: ", advres)

def cc(n, mi, ma):
    if mi <= int(n) <= ma:
        return True
    else:
        return False


def advancedcheck(ll):
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """
    count = 0
    checked_list = []
    cm_or_in_patt = "(\d{2,3})(\w{2})"
    hcl_patt = "#[\d(a-f)]{6}$"
    pid_patt = "\d{9}$"
    ecl_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for d in ll:
        keylist = ['byr',
                   'iyr',
                   'eyr',
                   'hgt',
                   'hcl',
                   'ecl',
                   'pid',
                   'cid']
        for key in d:
            if key in keylist:
                keylist.pop(keylist.index(key))
        if len(keylist) == 0 or len(keylist) == 1 and keylist[0] == 'cid':
            checked_list.append(d)
    for k, d in enumerate(checked_list):
        if not cc(d["byr"], 1920, 2002):
            continue
        if not cc(d["iyr"], 2010, 2020):
            continue
        if not cc(d["eyr"], 2020, 2030):
            continue
        if not re.match(cm_or_in_patt, d["hgt"]):
            continue
        length = re.findall(cm_or_in_patt, d["hgt"])
        print(length)
        if length[0][1] == "cm":
            if not cc(length[0][0], 150, 193):
                continue
        if length[0][1] == "in":
            if not cc(length[0][0], 59, 76):
                continue
        if re.match(hcl_patt, d["hcl"]) is None:
            continue
        if d["ecl"] in ecl_list:
            pass
        else:
            continue
        if re.match(pid_patt, d["pid"]) is None:
            continue
        count += 1

    print(count)
    return count




def check(ll):
    count = 0
    for d in ll:
        keylist = ['byr',
                   'iyr',
                   'eyr',
                   'hgt',
                   'hcl',
                   'ecl',
                   'pid',
                   'cid']
        for key in d:
            if key in keylist:
                keylist.pop(keylist.index(key))
        if len(keylist) == 0 or len(keylist) == 1 and keylist[0] == 'cid':
            count += 1
    return count


def parse(s):
    ll = []
    d = {}
    pattern = '(\w{3}):([\w#]*)'
    for row in s:
        if row == '':
            ll.append(d)
            d = {}
        else:
            res = re.findall(pattern, row)
            for kp in res:
                d[kp[0]] = kp[1]
    return ll

if __name__ == '__main__':
    print(main())
