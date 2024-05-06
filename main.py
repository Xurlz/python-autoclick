#!/usr/bin/env python

import argparse
import pyautogui
from datetime import datetime
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('--time',required = True)
args = parser.parse_args()

format = '%H:%M:%S'

while datetime.now().strftime(format) != args.time:
    print(datetime.now().strftime(format))
    print(args.time)
    sleep(0.5)
    pass

pyautogui.click()

