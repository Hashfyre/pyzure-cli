#! /usr/bin/env python
"""
    Usage: pyzure storage container create [-h|--help] [options]

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


def main(argv):

    args = docopt(
        __doc__,
        argv=argv,
        version='pyzure-cli version 0.0.0'
        # options_first=True
    )

    if '<args>' in args.keys():
        argv = args['<args>']
    else:
        main(['--help'])


if __name__ == '__main__':
    print(docopt(__doc__))
    main(sys.argv[1:])
