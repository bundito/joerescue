"""

+-----------------------------------+
|  GUNICORN CONFIG FOR RADIOCLASH   |
+-----------------------------------+

Please don't break this.

"""

import multiprocessing

bind = "0.0.0.0:6543"    # was Pyramid binding
workers = multiprocessing.cpu_count() * 2 + 1

reload = True       # reload on code changes; may have to disable later
--reload-engine inotify

