# -*- coding: utf-8 -*-
#
# Copyright © 2013 Pierre Raybaut
# Licensed under the terms of the MIT License

"""
imageplotplugin
===============

A guiqwt image widget plugin for Qt Designer
"""

from guiqwt.qtdesigner import create_qtdesigner_plugin
Plugin = create_qtdesigner_plugin("guiqwt", "guiqwt.plot", "ImageWidget",
                                  icon="image.png")
