#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

sys.path.append(os.getcwd() + '/src')

from src import App

try:
    App = App.App()
    App.run()
except Exception as e:
    print("Error: %s" % str(e))
