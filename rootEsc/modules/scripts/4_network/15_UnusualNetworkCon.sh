#!/bin/bash

# Author: Pevinkumar A
# Last Update: 29-03-2025
# Description: Enumerate unusal network connections.

netstat -tunapl | grep -v "127.0.0.1"
