import os
import subprocess

import pytube

yt = pytube.YouTube("https://www.youtube.com/watch?v=WH7xsW5Os10")
vids = yt.streams.all()

for i in range(len(vids)):
    print(i, '. ', vids[i])
