# -*- coding: utf-8 -*-
#
# Copyright © 2013 Pierre Raybaut
# Licensed under the terms of the MIT License

"""
plotplugin
==========

A guiqwt plot widget plugin for Qt Designer
"""

from guiqwt.qtdesigner import create_qtdesigner_plugin
Plugin = create_qtdesigner_plugin("guiqwt", "guiqwt.plot", "CurveWidget",
                                  icon="curve.png")
