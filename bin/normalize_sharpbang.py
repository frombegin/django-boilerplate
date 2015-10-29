#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
import os

if len(argv) != 2:
    print "usage: %s [dir]" % os.path.basename(__file__)
    exit(0)

for top, dirs, files in os.walk(argv[1]):

    for f in files:
        fn = os.path.join(top, f)
        _, ext = os.path.splitext(fn)
        if ext == '.py':
            with open(fn) as f:
                pass
                # linecounter = 1
                # for line in f:
                #     if linecounter==1:
                #         if not line.startswith('#!'):
                #            pass # 写入sharpbang, 写入 utf-8
                #     else:
                #         print line
                #
                # linecounter += 1
                # print f.readlines(2)[0:2]
                # print '-'*60

