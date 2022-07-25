# -*- coding: utf-8 -*-
"""
Install and manage python packages

usage: pip.py [-h] [--verbose] sub-command ...

optional arguments:
  -h, --help    show this help message and exit
  --verbose     be more chatty

List of sub-commands:
    sub-command     "pip sub-command -h" for more help on a sub-command
        list        list packages installed
        install     install packages
        download    download packages
        search      search with the given word fragment
        versions    find versions available for the given package
        uninstall   uninstall packages
        update      update an installed package
"""
import pip._internal
import importlib.util
import sys

# https://stackoverflow.com/questions/67631/how-do-i-import-a-module-given-the-full-path
spec = importlib.util.spec_from_file_location('pip', 'TODO determine path')
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

pip._internal.main("TODO pop the arguments to this script")