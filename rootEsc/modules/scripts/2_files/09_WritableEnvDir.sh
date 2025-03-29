#!/bin/bash

# Author: Pevinkumar A
# Last Update: 29-03-2025
# Description: Enumerate read and write permission folders from PATH env.

echo $PATH | tr ":" "\n" | xargs -I {} find {} -maxdepth 0 -type d -perm -u=rw 2>/dev/null