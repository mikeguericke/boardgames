#!/usr/bin/python

import os
import test

number=0

x=int(raw_input("How many times should I test?: "))
for i in range(x):
        number =  int(test.main())/x

print number
