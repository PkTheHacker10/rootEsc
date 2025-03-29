#!/bin/bash

# Author: Pevinkumar A
# Last Update: 29-03-2025
# Description: Enumerate crontab tasks.

cat /etc/crontab | grep -v '^#'