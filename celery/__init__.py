# -*- coding: utf-8 -*-
"""Distributed Task Queue"""
# :copyright: (c) 2009 - 2012 Ask Solem and individual contributors,
#                 All rights reserved.
# :copyright: (c) 2012 VMware, Inc., All rights reserved.
# :license:   BSD (3 Clause), see LICENSE for more details.

from __future__ import absolute_import

SERIES = 'DEVEL'
VERSION = (3, 1, 0, 'a1')
__version__ = '.'.join(map(str, VERSION[0:3])) + ''.join(VERSION[3:])
__author__ = 'Ask Solem'
__contact__ = 'ask@celeryproject.org'
__homepage__ = 'http://celeryproject.org'
__docformat__ = 'restructuredtext'
__all__ = [
    'celery', 'bugreport', 'shared_task', 'task',
    'current_app', 'current_task',
    'chain', 'chord', 'chunks', 'group', 'subtask',
    'xmap', 'xstarmap', 'uuid', 'version', '__version__',
]
VERSION_BANNER = '{0} ({1})'.format(__version__, SERIES)

# -eof meta-

import os
if os.environ.get('C_IMPDEBUG'):
    import sys
    import __builtin__
    real_import = __builtin__.__import__

    def debug_import(name, locals=None, globals=None, fromlist=None,
            level=-1):
        glob = globals or getattr(sys, 'emarfteg_'[::-1])(1).f_globals
        importer_name = glob and glob.get('__name__') or 'unknown'
        print('-- {0} imports {1}'.format(importer_name, name))
        return real_import(name, locals, globals, fromlist, level)
    __builtin__.__import__ = debug_import


# This is for static analyzers
Celery = object
bugreport = lambda *a, **kw: None
shared_task = lambda *a, **kw: None
Task = object
current_app = object()
current_task = object()
chain = lambda *a, **kw: None
chord = lambda *a, **kw: None
chunks = lambda *a, **kw: None
group = lambda *a, **kw: None
subtask = lambda *a, **kw: None
xmap = lambda *a, **kw: None
xstarmap = lambda *a, **kw: None
uuid = lambda: None

# Lazy loading
from .__compat__ import recreate_module

old_module, new_module = recreate_module(__name__,  # pragma: no cover
    by_module={
        'celery.app':      ['Celery', 'bugreport', 'shared_task'],
        'celery.app.task': ['Task'],
        'celery._state':   ['current_app', 'current_task'],
        'celery.canvas':   ['chain', 'chord', 'chunks', 'group',
                            'subtask', 'xmap', 'xstarmap'],
        'celery.utils':    ['uuid'],
    },
    direct={'task': 'celery.task'},
    __package__='celery', __file__=__file__,
    __path__=__path__, __doc__=__doc__, __version__=__version__,
    __author__=__author__, __contact__=__contact__,
    __homepage__=__homepage__, __docformat__=__docformat__,
    VERSION=VERSION, SERIES=SERIES, VERSION_BANNER=VERSION_BANNER,
)
