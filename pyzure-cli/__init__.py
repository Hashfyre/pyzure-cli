#! /usr/bin/env python

import sys
from importlib import import_module

if __name__ == '__main__':
    import_module('pyzure-cli').main(sys.argv[1:])
