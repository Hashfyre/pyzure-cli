"""
    Usage: storage container create [options] [container]

    Options:
    -h, --help                                  output usage information
    -v, --verbose                               use verbose output
    --json                                      use json output
    --container <container>                     the storage container name
    -p, --permission <permission>               the storage container ACL permission(Off/Blob/Container)
    -a, --account-name <accountName>            the storage account name
    -k, --account-key <accountKey>              the storage account key
    -c, --connection-string <connectionString>  the storage connection string
    -vv                                         run storage command in debug mode
"""

import sys
import os
from importlib import import_module
from docopt import docopt

# sys.path.append('./storage')
# commands = {command: import_module(command).main for command in [
#     # 'account',
#     # 'blob',
#     'container',
#     # 'cors',
#     # 'directory',
#     # 'file',
#     # 'logging',
#     # 'metrics',
#     # 'queue',
#     # 'share',
#     # 'table
# ]}


def main(argv):

    args = docopt(
        __doc__,
        argv=argv,
        version='pyzure-cli version 0.0.0'
    )

    sys.stdout.write("".format(args))
    # command = args['<command>']
    # argv = [command] + args['<args>']
    # if command in commands:
    #     commands[command](argv)
    # else:
    #     main(['--help'])


if __name__ == '__main__':
    main(sys.argv[1:])
