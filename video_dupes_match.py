#!/usr/bin/python3

import argparse
import os
import pathlib
import cv2
import numpy
import json
import sys
import math

parser = argparse.ArgumentParser(description="Match fingerprints", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--input', help='A file name to read the fingerprints from', default='fingerprints.json')
parser.add_argument('--output', help='A file name to write the sorted match results to', default='matches.json')
parser.add_argument('--threshold', help='A distance threshold above which matches are ignored', default=20.0, type=float)

args = parser.parse_args()

def distance(fingerprints1, fingerprints2):
    if len(fingerprints1) != len(fingerprints2):
        return sys.float_info.max
    the_sum = 0
    for index in range(0,len(fingerprints1)):
        for channel in [0, 1, 2]:
            the_sum += pow(fingerprints1[index][channel] - fingerprints2[index][channel], 2)
    return math.sqrt(the_sum)

file_pairs = []
distances = []
with open(args.input) as f:
    fingerprints_map = json.loads(f.read())
    keys = list(fingerprints_map.keys())
    for index1 in range(0, len(keys)):
        for index2 in range(index1+1, len(keys)):
            d = distance(fingerprints_map[keys[index1]], fingerprints_map[keys[index2]])
            if d > args.threshold:
                continue
            file_pairs.append([keys[index1], keys[index2]])
            distances.append(d)
            # print('{} - {} / {}'.format(d, keys[index1], keys[index2]))

sorted_indices = list(numpy.argsort(distances))

matches = []
for index in sorted_indices:
    matches.append([distances[index], file_pairs[index][0], file_pairs[index][1]])

with open(args.output, "w") as f:
    f.write(json.dumps(matches, indent=4))
