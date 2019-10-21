# video_dupes

A super braindead collection of tools to find some gross duplicates in a medium size
collection of video files.

CAUTION: Do not trust this tool at all! It is riddled with bugs! Do not use it :)

That said: It works for me..

- It works by taking a couple of frames from a video file (see the --time parameter
of the video_dupes_fingerprint.py tool) and calculates their mean RGB value. This
tool finally write a json file containing these fingerprints.

- In a matching step (video_dupes_match.py) a euclidian distance is calculated by this long vector
of RGB triplets between all pairs of two entries in the fingerprints json file.
The distances are sorted and a new output file is generated with the (sorted) scores
and corresponding file names.

- In a cleaning step (video_dupes_clean.py) the sorted output of the matching step is presented to the
user as binary choices of which of the two videos to keep. The result of this step is
a text file with file names which are to be deleted.

- The last step is reviewing the list of files to delete and finally 
deleting them (empty_trash.sh).

This is an example session of the files:

<pre>
./video_dupes_fingerprint.py --path /home/user/Downloads /media/storage/Stuff
[...]
./video_dupes_match.py
[...]
./video_dupes_clean.py
[...interactive prompts...]
./empty_trash.sh
</pre>

<pre>
usage: video_dupes_fingerprint.py [-h] [--path PATH [PATH ...]]
                                  [--extension EXTENSION [EXTENSION ...]]
                                  [--output OUTPUT] [--time TIME [TIME ...]]

Fingerprint video files

optional arguments:
  -h, --help            show this help message and exit
  --path PATH [PATH ...]
                        A path to a tree containing video files (default:
                        ['.'])
  --extension EXTENSION [EXTENSION ...]
                        A file name extension to treat as movie file (default:
                        ['.mp4', '.avi', '.mpg', '.mpeg', '.wmv', '.mov',
                        '.mkv', '.flv', '.m4v', '.mp7'])
  --output OUTPUT       A file name to store the fingerprints to (default:
                        fingerprints.json)
  --time TIME [TIME ...]
                        The times (in seconds) into the video where to produce
                        a fingerprint (default: [30, 60, 90, 120])


usage: video_dupes_match.py [-h] [--input INPUT] [--output OUTPUT]

Match fingerprints

optional arguments:
  -h, --help       show this help message and exit
  --input INPUT    A file name to read the fingerprints from (default:
                   fingerprints.json)
  --output OUTPUT  A file name to write the sorted match results to (default:
                   matches.json)



usage: video_dupes_clean.py [-h] [--input INPUT] [--output OUTPUT]
                            [--player PLAYER]

Assemble trash list

optional arguments:
  -h, --help       show this help message and exit
  --input INPUT    A file name to read the sorted match results from (default:
                   matches.json)
  --output OUTPUT  A file name to write filenames marked for deletion to
                   (default: trash.txt)
  --player PLAYER  A program to play a video file (default: mplayer)
</pre>
