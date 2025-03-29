#!/bin/bash

# Author: Pevinkumar A
# Last Update: 29-03-2025
# Description: Enumerate process that running from suspecious location.

ps aux | grep "/tmp\|/dev/shm"