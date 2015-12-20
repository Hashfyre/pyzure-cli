"""
usage: pyzure storage metrics [-h|--help] [<command>...]

options:
    -h, --help

Commands to manage your Storage metrics properties
    storage metrics show [options]
    storage metrics set [options]
"""

import sys
from importlib import import_module
from docopt import docopt

sys.path.append('./metrics')
commands = {command: import_module(command).main for command in [
    'show',
    'set'
]}


def main(argv):

    args = docopt(
        __doc__,
        argv=argv,
        version='pyzure-cli version 0.0.0'
    )

    command = args['<command>']
    argv = [command] + args['<args>']
    if command in commands:
        commands[command](argv)
    else:
        main(['--help'])


if __name__ == '__main__':
    main(sys.argv[1:])
