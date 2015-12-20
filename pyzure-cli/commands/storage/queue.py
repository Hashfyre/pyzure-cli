"""
usage: pyzure storage queue [-h|--help] [<command>...]

options:
    -h, --help

Commands to manage your Storage queues
    storage queue create [options] [queue]
    storage queue list [options] [prefix]
    storage queue show [options] [queue]
    storage queue delete [options] [queue]

Commands to manage shared access signatures of your Storage queue
    storage queue sas create [options] [queue] [permissions] [expiry]

Commands to manage stored access policies of your Storage queue
    storage queue policy create [options] [queue] [name]
    storage queue policy show [options] [queue] [name]
    storage queue policy list [options] [queue]
    storage queue policy set [options] [queue] [name]
    storage queue policy delete [options] [queue] [name]
"""

import sys
from importlib import import_module
from docopt import docopt

sys.path.append('./queue')
commands = {command: import_module(command).main for command in [
    'create',
    'list',
    'show'
    'delete'
    'sas',
    'policy'
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
