#!/bin/bash

# Author: Pevinkumar A
# Last Update: 29-03-2025
# Description: Enumerate root privileged users.

awk -F: '($3 == "0") {print}' /etc/passwd