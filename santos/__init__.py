__author__ = 'anderson'
import sys

if sys.version_info < (3, 2):
    from santos import *
else:
    from santos.santos import TaskScheduling, stopjobs


