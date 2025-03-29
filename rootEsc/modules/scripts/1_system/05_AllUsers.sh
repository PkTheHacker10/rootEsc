#!/bin/bash

# Author: Pevinkumar A
# Last Update: 29-03-2025
# Description: Enumerate all users.

cat /etc/passwd | cut -d ":" -f 1