#!/usr/bin/env python
# coding: utf-8
from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["utils.py", "saw.py"]

setup(name = "datools",
    version = "1.0",
    description = "Utilities that I always want to have",
    author = "David Österberg",
    author_email = "david.osterberg@husqvarnagroup.com",
    url = "http://www.husqvarna.se",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = ['datools'],
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    long_description = """Utilities for plotting and data processing that I always want to have handy.""" 
) 
