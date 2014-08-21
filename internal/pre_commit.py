#!/usr/bin/env python3
## INFO ########################################################################
##                                                                            ##
##                                   cutils                                   ##
##                                   ======                                   ##
##                                                                            ##
##                     Modern and Lightweight C Utilities                     ##
##                       Version: 0.8.90.725 (20140821)                       ##
##                                                                            ##
##                        File: internal/pre_commit.py                        ##
##                                                                            ##
##           Designed and written by Peter Varo. Copyright (c) 2014           ##
##             License agreement is provided in the LICENSE file              ##
##                 For more info visit: http://www.cutils.org                 ##
##                                                                            ##
######################################################################## INFO ##

# import Python modules
from sys import exit as sys_exit

# Import yaml modules
from yaml import load as yaml_load
try:
    from yaml import CLoader as yaml_Loader
except ImportError:
    from yaml import yaml_Loader

# Import cutils modules
from cutils.cver import version
from cutils.cdoc import document
from cutils.ccom import collect
from cutils.clic import header

# TODO: generate documentation to some better place, maybe /tmp ?
#       after committed, change the branch copy the content and
#       then commit changed to the gh-pages branch and switch
#       back to master branch

# TODO: Make error messages and reports of cver/cdoc/ccom/clic similar!

version(sub_max=9,
        rev_max=99,
        build_max=999)

document(infolder='doc/src',
         outfolder='../../../temporary_stuffs/cutils',
         extension='.yaml',
         loader=lambda s: yaml_load(s, Loader=yaml_Loader))

collect('.')
header('.')

sys_exit('pre-commit: success\n')
