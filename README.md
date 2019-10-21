# video_dupes

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

Match fingerprints

optional arguments:
  -h, --help       show this help message and exit
  --input INPUT    A file name to read the sorted match results from (default:
                   matches.json)
  --output OUTPUT  A file name to write filenames marked for deletion to
                   (default: trash.txt)
  --player PLAYER  A program to play a video file (default: mplayer)
</pre>
