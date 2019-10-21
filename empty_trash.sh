cat trash.txt | while read line; do rm -f "$line"; done
