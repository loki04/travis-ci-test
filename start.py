#!/usr/bin/env python

import platform
import psutil

print "Start"

print platform.platform()

print psutil.virtual_memory()

print "Done"
