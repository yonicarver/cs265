# python 3.5
# -----------------------------------------------------------------------------
# Yonatan Carver
# CS 265 - Advanced Programming
# Lab 04
# -----------------------------------------------------------------------------
# Q2.1 Look at the students input file in the directory. Write a Python program
# that, for each student, computes the average of all the scores for that student,
# prints 2 columns: the name, followed by the average. Submit s1.py.
# -----------------------------------------------------------------------------

from sys import argv

def average(nums):
    ''' Compute average of list of numbers '''
    return sum(nums)/len(nums)

with open(argv[1], 'r') as f:
    lines = [line.strip() for line in f]

    nums = []
    for item in range(len(lines)):
        nums.append([int(s) for s in lines[item].split() if s.isdigit()])

    averages = []
    for i in nums:
        averages.append(average(i))

    names = []
    for i in lines:
        names.append(i.split(' ', 1)[0])

    together = zip(names, averages)

    print('NAME','\t', 'AVERAGE')
    print('------------------')
    for item in together:
        print('%s \t %.2f' % (item[0], item[1]))

