"""
usage: pyzure storage cors [-h|--help] [<command>...]

options:
    -h, --help

Commands to manage your Storage CORS (Cross-Origin Resource Sharing)
    storage cors set [options]
    storage cors show [options]
    storage cors delete [options]

"""

import sys
from importlib import import_module
from docopt import docopt

sys.path.append('./cors')
commands = {command: import_module(command).main for command in [
    'set',
    'show',
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
