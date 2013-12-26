# -*- coding: utf-8 -*-
#
# Copyright © 2013 Pierre Raybaut
# Licensed under the terms of the MIT License

"""
matplotlibplugin
================

A Matplotlib widget plugin for Qt Designer
"""

import os.path as osp

from matplotlib import rcParams
rcParams['font.size'] = 9

from guiqwt.qtdesigner import create_qtdesigner_plugin
Plugin = create_qtdesigner_plugin("Matplotlib", "matplotlibwidget",
              "MatplotlibWidget",
              icon=osp.join(rcParams['datapath'], 'images', 'matplotlib.png'))