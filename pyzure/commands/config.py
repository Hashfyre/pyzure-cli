
"""
usage: pyzure config [-h|--help] [<command>...]

options:
    -h, --help

Commands to manage your local settings

List config settings
    config list [options]

Delete a config setting
    config delete [options] <name>

Update a config setting
    config set <name> <value>

Sets the cli working mode, valid names are 'arm' for resource manager and 'asm' for service management
    config mode [options] <name>
"""

import sys
from importlib import import_module
from docopt import docopt

sys.path.append('./config')
commands = {command: import_module(command).main for command in [
    'list',
    'delete',
    'set',
    'mode'
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
