"""
usage: pyzure storage account [-h|--help] [<command>...]

options:
    -h, --help

storage account list [options]
    storage account show [options] <name>
    storage account create [options] <name>
    storage account set [options] <name>
    storage account delete [options] <name>
    storage account check [options] <name>

Commands to manage your Storage account keys
    storage account keys list [options] <name>
    storage account keys renew [options] <name>

Commands to show your Storage connection string
    storage account connectionstring show [options] <name>

"""

import sys
from importlib import import_module
from docopt import docopt

sys.path.append('./account')
commands = {command: import_module(command).main for command in [
    'show',
    'create',
    'set',
    'delete',
    'check',
    'keys',
    'connectionstring'
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
