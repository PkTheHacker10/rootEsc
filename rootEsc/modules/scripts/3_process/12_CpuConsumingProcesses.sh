#!/bin/bash

# Author: Pevinkumar A
# Last Update: 29-03-2025
# Description: Enumerate Top 10 process that consume high cpu.

ps -au --sort=-pcpu | head