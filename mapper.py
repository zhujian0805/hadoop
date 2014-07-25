#!/usr/bin/env python

import sys
import re


fo = open("test01.cfg")
pattern = ""

while True:
  line = fo.readline()
  if line:
    pattern = line.strip()
  else:
    break


for line in sys.stdin:
  line = line.strip()
  keys = line.split()
  for key in keys and re.search(pattern, key):
    value = 1
    print( "%s\t%d" % (key, value) )
