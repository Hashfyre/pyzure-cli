#! /usr/bin/env python
"""
usage: pyzure storage container [-h|--help] [<command> [<args>...]]

options:
    -h, --help
    
Commands to manage your Storage containers
    storage container (create|delete|set|show) [options] [container]
    storage container list [options] [prefix]

Commands to manage shared access signatures of your Storage container
    storage container sas create [options] [container] [permissions] [expiry]

Commands to manage stored access policies of your Storage container
    storage container policy (create|delete|set|show) [options] [container] [name]
    storage container policy list [options] [container]
"""

import sys
import os
from importlib import import_module
from docopt import docopt

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
        version='pyzure-cli version 0.0.0',
        # options_first=True
    )

    command = args['<command>']
    
    if '<args>' not in args.keys():
        main(['--help'])

    if command in commands:
        commands[command](argv)
    else:
        main(['--help'])


if __name__ == '__main__':
    print(docopt(__doc__))
    main(sys.argv[1:])
