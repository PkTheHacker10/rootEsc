#!/bin/bash

# Author: Pevinkumar A
# Last Update: 29-03-2025
# Description: Sudo password check.

sudo -ln

if [ $? -eq 1 ]; then
    echo "     Password required. If you know the password, don't forget to try (sudo -l) with the password."
fi