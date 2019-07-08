#!/usr/bin/env python
"""mapper.py"""

import sys

nhl = ['nhl','playoff','game','stanleycup','nhlplayoffs','hockey','pick','first','team','stanleycupplayoffs']
s = ''
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        if word in nhl:
            for w in words:
                if w!=word and w in nhl:
                    s = word+'-'+w
                    print '%s\t%s' % (s,1)
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        #print '%s\t%s' % (word, 1)