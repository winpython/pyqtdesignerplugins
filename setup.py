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

setup(name='PyQtdesignerplugins', version='1.0',
      description='PyQtdesignerplugins installs Qt Designer plugins for PyQt4',
      long_description="""PyQtdesignerplugins installs Python Qt designer plugins (Matplotlib, guiqwt, ...) in PyQt4 directory""", 
      py_modules = ['matplotlibwidget'],
      data_files=[(r'Lib\site-packages\PyQt4\plugins\designer\python', get_data_files('plugins'))],
      requires=["PyQt4 (>4.3)",],
      author = "Pierre Raybaut",
      author_email = 'pierre.raybaut@gmail.com',
      url = 'http://code.google.com/p/winpython/',
      classifiers=['Operating System :: Microsoft :: Windows'])
