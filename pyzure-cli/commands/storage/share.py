"""
usage: pyzure storage [-h|--help] [<command>...]

options:
    -h, --help

Commands to manage your Storage file shares
    storage share create [options] [share]
    storage share show [options] [share]
    storage share set [options] [share]
    storage share delete [options] [share]
    storage share list [options] [prefix]

Commands to manage shared access signatures of your Storage file shares
    storage share sas create [options] [share] [permissions] [expiry]

Commands to manage stored access policies of your Storage file share
    storage share policy create [options] [share] [name]
    storage share policy show [options] [share] [name]
    storage share policy list [options] [share]
    storage share policy set [options] [share] [name]
    storage share policy delete [options] [share] [name]
"""

import sys
from importlib import import_module
from docopt import docopt

sys.path.append('./share')
commands = {command: import_module(command).main for command in [
    'create',
    'show',
    'set',
    'delete',
    'list',
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
