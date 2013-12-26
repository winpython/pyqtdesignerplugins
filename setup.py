# -*- coding: utf-8 -*-
"""PyQt Designer Plugins"""

from distutils.core import setup
import os
import os.path as osp

def get_data_files(dirname):
    """Return data files in directory *dirname*"""
    flist = []
    for dirpath, _dirnames, filenames in os.walk(dirname):
        for fname in filenames:
            flist.append(osp.join(dirpath, fname))
    return flist

PROJECT_NAME = 'PyQtdesignerplugins'

setup(name=PROJECT_NAME, version='1.1',
      description='%s installs Qt Designer plugins for PyQt4' % PROJECT_NAME,
      long_description="""%s installs Python Qt designer plugins (Matplotlib, guiqwt, ...) in PyQt4 directory.

%s is part of the WinPython distribution project.
""" % (PROJECT_NAME, PROJECT_NAME), 
      py_modules = ['matplotlibwidget'],
      data_files=[(r'Lib\site-packages\PyQt4\plugins\designer\python', get_data_files('plugins'))],
      requires=["PyQt4 (>4.3)", "guiqwt (>2.0)",],
      author = "Pierre Raybaut",
      author_email = 'pierre.raybaut@gmail.com',
      url = 'http://winpython.sourceforge.net/',
      classifiers=['Operating System :: Microsoft :: Windows'])
