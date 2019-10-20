#!/usr/bin/python3

import argparse
import os
import pathlib
import cv2
import numpy
import json

parser = argparse.ArgumentParser(description="Fingerprint video files", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--path', help='A path to a tree containing video files', nargs='+', default=['.'])
parser.add_argument('--extension', help='A file name extension to treat as movie file', nargs='+', default=['.mp4', '.avi', '.mpg', '.mpeg', '.wmv', '.mov', '.mkv', '.flv', '.m4v', '.mp7'])
parser.add_argument('--output', help='A file name to store the fingerprints to', default='fingerprints.json')
parser.add_argument('--time', help='The times (in seconds) into the video where to produce a fingerprint', nargs='+', default=[30, 60, 90, 120], type=float)

args = parser.parse_args()

files = []
print('Assembling file list...')
for path in args.path:
    print('Processing path "{}"...'.format(path))
    for dir_name, subdir_list, file_list in os.walk(path):
        print('Directory "{}"...'.format(dir_name))
        for file_name in file_list:
            full_file_name = os.path.join(dir_name, file_name)
            suffix = pathlib.Path(full_file_name).suffix.lower()
            # print('Suffix is {}'.format(suffix))
            if suffix in args.extension:
                files.append(full_file_name)
            else:
                print('Ignored suffix "{}" on file "{}"'.format(suffix, full_file_name))

fingerprints = {}
count = 0
for file_name in files:
    # if count == 10:
    #    break
    print('Processing "{}"...'.format(file_name))
    video_capture = cv2.VideoCapture(file_name)
    if not video_capture.isOpened():
        print('Failed to open video file "{}"'.format(file_name))
        continue
    image_means = []
    for time in args.time:
        video_capture.set(cv2.CAP_PROP_POS_MSEC, 1000.0 * time)
        success, image = video_capture.read()
        if success:
            image_mean = image.mean(axis=0).mean(axis=0)
            image_means.append(image_mean.tolist())
    fingerprints[file_name] = image_means
    count = count + 1

with open(args.output, 'w') as f:
    f.write(json.dumps(fingerprints, indent=4))
