#!/usr/bin/python2.7

# python 2.7.12
# Ubuntu 16.04.3 LTS -- xenial

# Yonatan Carver
# CS 265 - Advanced Programming Techniques
# Assignment 02

# -----------------------------------------------------------------------------

import json
import urllib
from sys import argv
from getopt import getopt
import math
import random

# get json from web
response = urllib.urlopen('http://www3.septa.org/hackathon/Stops/?req1=23')
septa_data = json.load(response)

# get command line arguments after '-n'
n_args = 5       # default
myopts, args = getopt(argv[1:],"n:")
for flag, arg in myopts:
    if  flag == '-n':
        n_args = arg

# from file: philly_loc.py ----------------------------------------------------

min_lat = 39.9155802878
max_lat = 40.1026872756
min_long = -75.2388309423
max_long = -74.9699425597

lat_delta = max_lat - min_lat
long_delta = max_long - min_long

mult = 1000

def getLoc() :
	'''Returns some location in Phila.
	[LAT, LONG], in decimal degrees'''

	x = random.randint( 0, int(long_delta*mult) )
	y = random.randint( 0, int(lat_delta*mult) )

	return [ min_lat + y/float(mult) , min_long + x/float(mult) ]

# -----------------------------------------------------------------------------

(my_loc_lat, my_loc_lng) = getLoc()     # user's current location in PHL

def get_dist():
    """ calculate euclidian distance between current loc & stop (lat, lng) """
    return math.sqrt(((my_loc_lat - stop_lat)**2) + ((my_loc_lng - stop_lng)**2))

# calculate euclidian distances for each stop
for i in range(len(septa_data)):
    stop_lat = float(septa_data[i]['lat'])
    stop_lng = float(septa_data[i]['lng'])
    septa_data[i]['e_dist'] = float(get_dist()) # add a field for euclidian distance for each entry

# sort euclidian distances for each stop (ascending order)
sorted_septa_data = sorted(septa_data, key = lambda septa_data: septa_data['e_dist'])

# print location information
# format: DISTANCE  LOCATION  (LAT, LONG)
for i in range(int(n_args)):
    distance = float(sorted_septa_data[i]['e_dist'])
    location = sorted_septa_data[i]['stopname'].replace('&amp;','&')
    lat = float(sorted_septa_data[i]['lat'])
    lng = float(sorted_septa_data[i]['lng'])
    print("%.7f \t %s \t\t (%.7f,%.7f)" % (distance, location, lat, lng))
