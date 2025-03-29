#!/bin/bash

# Author: Pevinkumar A
# Last Update: 29-03-2025
# Description: Enumerate SUID bins.

find / -type f -perm -04000 2>/dev/null