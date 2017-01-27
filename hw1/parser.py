__author__ = 'paul'
from data import *

def parsefile(filepath):
    result = []
    for line in open(filepath, 'r'):
        if (line.startswith('(') or line == '\n'):
            print("header skipped")
        else:
            row = parseline(line)
            result.append(row)
    return result


def parseline(line):
    line = line.replace(' ', '')
    line = line.replace('\n', '')
    line = line.replace(';', '')
    line = line.split(':')[1]
    rawattr = line.split(',')
    size = rawattr[0]
    occupied = rawattr[1]
    price = rawattr[2]
    music = rawattr[3]
    location = rawattr[4]
    vip = rawattr[5]
    beer = rawattr[6]
    enjoyed = rawattr[7]
    result = Row(size, occupied, price, music, location, vip, beer, enjoyed)
    return result