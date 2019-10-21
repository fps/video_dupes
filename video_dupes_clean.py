#!/usr/bin/python3

import argparse
import os
import pathlib
import cv2
import numpy
import json
import sys
import math
import subprocess
import send2trash

parser = argparse.ArgumentParser(description="Match fingerprints", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--input', help='A file name to read the sorted match results from', default='matches.json')
parser.add_argument('--output', help='A file name to write filenames marked for deletion to', default='trash.txt')
parser.add_argument('--player', help='A program to play a video file', default="mplayer")

args = parser.parse_args()

file_pairs = []
distances = []
trash=[]
with open(args.input) as f:
    matches = json.loads(f.read())
    really_done = False
    for match in matches:
        if not (os.path.isfile(match[1]) and os.path.isfile(match[2])):
            continue

        done = False
        while not done:
            print('Score: {}'.format(match[0]))
            print('1: {}'.format(match[1]))
            print('2: {}'.format(match[2]))
            print('Enter: Both')
            print('p: Play back both after each other')
            print('q: Quit')
            print('Keep (1/2/Both)?')
            x = input()
            if x == "q":
                really_done = True
                done = True


            if x == "":
                done = True

            if x == "p":
                subprocess.call([args.player, match[1]])
                subprocess.call([args.player, match[1]])
                
            if x == "1":
                trash.append(match[2])
                done = True

            if x == "2":
                trash.append(match[1])
                done = True

        if really_done:
            break

with open(args.output, "w") as f:
    for file_name in trash:
        f.write('{}\n'.format(file_name)) 
