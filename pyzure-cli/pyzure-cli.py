#! /usr/bin/env python
"""
usage: pyzure-cli [-h|--help] [<command> [<args>...]]

options:
    -h, --help
    -v, --version

"""

import sys
from importlib import import_module
from docopt import docopt

sys.path.append('./commands')
commands = {command: import_module(command).main for command in [
    'hullo'
]}


def main(argv):

    args = docopt(
        __doc__,
        argv=argv,
        version='pyzure-cli version 0.0.0',
        options_first=True
    )

    command = args['<command>']
    argv = [command] + args['<args>']
    if command in commands:
        commands[command](argv)
    else:
        main(['--help'])


if __name__ == '__main__':
    main(sys.argv[1:])
