#!/bin/bash

# Author: Pevinkumar A
# Last Update: 29-03-2025
# Description: Enumerate process that runing with root privilege.

ps aux | awk '$1 == "root" && $2 $11 !~ "systemd|bash|sshd" {print "User: " $1 " - ","PID: " $2 ,"Proc_CMD: " $11} '