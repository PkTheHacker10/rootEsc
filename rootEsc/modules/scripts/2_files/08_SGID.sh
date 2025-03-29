#!/bin/bash

# Author: Pevinkumar A
# Last Update: 29-03-2025
# Description: Enumerate SGID bins.

find / -type f -perm -02000 2>/dev/null