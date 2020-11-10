# python 3.5
# -----------------------------------------------------------------------------
# Yonatan Carver
# CS 265 - Advanced Programming
# Lab 04
# -----------------------------------------------------------------------------
# Q2.2 Same thing, but the input file will be a CSV. Submit s2.py.
# -----------------------------------------------------------------------------

from sys import argv

def average(nums):
    ''' Compute average of list of numbers '''
    return sum(nums)/len(nums)


with open(argv[1], 'r') as f:
    lines = [line.strip() for line in f]

    newlines = []
    for i in lines:
        newlines.append(i.replace(",",' '))

    nums = []
    for item in range(len(newlines)):
        # check to see if item is a digit and split them off
        nums.append([int(s) for s in newlines[item].split() if s.isdigit()])

    averages = []
    for i in nums:
        averages.append(average(i))

    names = []
    for i in newlines:
        names.append(i.split(' ', 1)[0])

    together = zip(names, averages)     # zip together names and averages

    print('NAME','\t', 'AVERAGE')
    print('------------------')
    for item in together:
        print('%s \t %.2f' % (item[0], item[1]))

