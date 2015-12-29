"""
usage: pyzure storage container [-h|--help] [<command>...]

options:
    -h, --help

Commands to manage your Storage containers
    storage container list [options] [prefix]
    storage container show [options] [container]
    storage container create [options] [container]
    storage container delete [options] [container]
    storage container set [options] [container]

Commands to manage shared access signatures of your Storage container
    storage container sas create [options] [container] [permissions] [expiry]

Commands to manage stored access policies of your Storage container
    storage container policy create [options] [container] [name]
    storage container policy show [options] [container] [name]
    storage container policy list [options] [container]
    storage container policy set [options] [container] [name]
    storage container policy delete [options] [container] [name]
"""

import sys
import os
from importlib import import_module
from docopt import docopt

# sys.path.append('./container')
sys.path.append(os.path.join(os.path.dirname(__file__), "container"))
commands = {command: import_module(command).main for command in [
    # 'list',
    # 'show',
    'create',
    # 'delete',
    # 'set',
    # 'sas',
    # 'policy'
]}


def main(argv):

    args = docopt(
        __doc__,
        argv=argv,
        version='pyzure-cli version 0.0.0'
        # options_first=True
    )

    command = args['<command>']
    argv = [command] + args['<args>']
    if command in commands:
        commands[command](argv)
    else:
        main(['--help'])


if __name__ == '__main__':
    main(sys.argv[1:])
