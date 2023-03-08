#!/usr/bin/env python3
import re
def rearrange_name(name):
  pattern = r"^([a-zA-Z]+), ([a-zA-z]+)$"
  names = re.search(pattern,name)
  print(names[2]+" "+names[1])

