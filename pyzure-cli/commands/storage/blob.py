"""
usage: pyzure storage blob [-h|--help] [<command>...]

options:
    -h, --help

Commands to manage your Storage blobs
    storage blob list [options] [container] [prefix]
    storage blob show [options] [container] [blob]
    storage blob delete [options] [container] [blob]
    storage blob upload [options] [file] [container] [blob]
    storage blob download [options] [container] [blob] [destination]

Commands to manage your blob copy operations
    storage blob copy start [options] [sourceUri] [destContainer]
    storage blob copy show [options] [container] [blob]
    storage blob copy stop [options] [container] [blob] [copyid]

Commands to manage shared access signature of your Storage blob
    storage blob sas create [options] [container] [blob]
"""

import sys
from importlib import import_module
from docopt import docopt

sys.path.append('./blob')
commands = {command: import_module(command).main for command in [
    'list',
    'show',
    'delete',
    'upload',
    'download',
    'copy',
    'sas'
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
