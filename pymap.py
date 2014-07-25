#!/usr/bin/env python

import sys
import re


fo = open("test01.cfg")
pattern = "root"

while True:
  line = fo.readline()
  if line:
    pattern = line.strip()
  else:
    break

fo.close()

for line in sys.stdin:
  line = line.strip()
  keys = line.split()
  for key in keys:
    if re.search(pattern, key):
      value = 1
      print( "%s\t%d" % (key, value) )
