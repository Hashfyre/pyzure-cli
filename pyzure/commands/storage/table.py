"""
usage: pyzure storage table [-h|--help] [<command>...]

options:
    -h, --help

Commands to manage your Storage tables
    storage table create [options] [table]
    storage table list [options] [prefix]
    storage table show [options] [table]
    storage table delete [options] [table]

Commands to manage shared access signatures of your Storage table
    storage table sas create [options] [table] [permissions] [expiry]

Commands to manage stored access policies of your Storage table
    storage table policy create [options] [table] [name]
    storage table policy show [options] [table] [name]
    storage table policy list [options] [table]
    storage table policy set [options] [table] [name]
    storage table policy delete [options] [table] [name]
"""

import sys
from importlib import import_module
from docopt import docopt

sys.path.append('./table')
commands = {command: import_module(command).main for command in [
    'create',
    'list',
    'show',
    'delete',
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
