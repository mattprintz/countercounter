#!/usr/bin/env python

from sys import argv

digimap = {
    '0': 0,
    '1': 1,
    '2': 1,
    '3': 1,
    '4': 1,
    '5': 1,
    '6': 1,
    '7': 2,
    '8': 1,
    '9': 1,
    '10': 1,
    '11': 3,
    '12': 1,
    '13': 2,
    '14': 2,
    '15': 2,
    '16': 2,
    '17': 3,
    '18': 2,
    '19': 2,
    '20': 2,
    '30': 2,
    '40': 2,
    '50': 2,
    '60': 2,
    '70': 3,
    '80': 2,
    '90': 2,
}

memo = {}

def digit(digit):
    return int(digimap.get(str(int(digit))))

def parse_set(num):
    num = str(num)
    num = '0' * (3-len(num)) + num
    if num in memo:
        return memo[num]
    syl = 0
    if num[0] != '0':
        syl += 2 #hundred
        syl += digit(num[0])
    if num[1] not in '01':
        syl += digit("%s0" % num[1])
    if num[1] == '1':
        syl += digit(num[1:])
    else:
        syl += digit(num[2])
    memo[num] = syl
    return syl

def calculate(number):
    syls = 0
    number = str(number)
    token = number
    sets = []
    while(token):
        sets.append(token[-3:])
        token = token[:-3]
    sets.reverse()
    syls += (2 * (len([s for s in sets[0:-2] if s != "000"]))) # thousand, million, billion, trillion = 2 sylables * set
    syls += sum(map(parse_set, sets))
    return syls

def total(count):
    count = int(count)
    i = 1
    total = 0
    while i <= count:
        if i % 1000 == 0:
            print i
        total += calculate(i)
        i += 1
    return total

num = argv[1]

print "TOTAL: %d" % total(num)

