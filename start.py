#!/usr/bin/env python

import platform
import psutil
import os

print platform.platform()
print psutil.virtual_memory()

f = os.statvfs(".")
print f.f_frsize * f.f_bavail
