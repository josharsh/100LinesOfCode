#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import os

p = re.compile(r'^\d\D.*?[.]mp3$')

def main():
    path = sys.argv[1]

    for file in os.listdir(path):
        print file
        m = p.match(file)
        if m:
            old_file = os.path.join(path, file)
            new_file = os.path.join(path, "0" + file)
            #raw_input(old_file + " " + new_file)
            os.rename(old_file, new_file)
            

if __name__ == "__main__":
	sys.exit(main())
