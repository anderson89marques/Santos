"""Santos"""
__version__ = '1.2.0'

import sys

if sys.version_info < (3, 2):
    from santos import *
else:
    from santos.santos import ThreadSchedule


