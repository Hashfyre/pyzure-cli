"""
usage: pyzure storage directory [-h|--help] [<command>...]

options:
    -h, --help

Commands to manage your Storage file directory
    storage directory create [options] [share] [path]
    storage directory delete [options] [share] [path]
"""

import sys
from importlib import import_module
from docopt import docopt

sys.path.append('./directory')
commands = {command: import_module(command).main for command in [
    'create',
    'delete'
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
