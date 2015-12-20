"""
usage: pyzure storage file [-h|--help] [<command>...]

options:
    -h, --help

Commands to manage your Storage files
    storage file list [options] [share] [path]
    storage file delete [options] [share] [path]
    storage file upload [options] [source] [share] [path]
    storage file download [options] [share] [path] [destination]

Commands to manage your file copy operations
    storage file copy start [options] [sourceUri] [destShare]
    storage file copy show [options] [share] [path]
    storage file copy stop [options] [share] [path] [copyid]

Commands to manage shared access signatures of your Storage file
    storage file sas create [options] [share] [path] [permissions] [expiry]

"""

import sys
from importlib import import_module
from docopt import docopt

sys.path.append('./file')
commands = {command: import_module(command).main for command in [
    'list',
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
