"""
usage: pyzure-cli hullo [-h|--help] [<name>]

options:
    -h, --help

"""

import sys
from docopt import docopt


def main(argv):

    args = docopt(
        __doc__,
        argv=argv,
        version='pyzure-cli version 0.0.0'
    )

    sys.stdout.write("Hullo {0}!".format(args['<name>'] or "World"))
