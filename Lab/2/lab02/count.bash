#!/bin/bash

# -------------------------------------
# Yoni Carver
# CS 265 - Advanced Programming
#
# 1/26/2018
# Ubuntu 16.04.3 LTS
#
# -------------------------------------

# prints filename, # of lines, and # of words for each file in cwd (excludes directories)


for file in *;
do
	if [ -f "$file" ] ; then
	wc=($(wc $file));
	lines=${wc[0]};
	words=${wc[1]};
	echo "$file $lines $words";
fi

done

