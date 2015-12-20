"""
usage: pyzure help [-h|--help] [<command>...]

options:
    -h, --help

"""

from docopt import docopt
from importlib import import_module


def main(argv):

    args = docopt(
        __doc__,
        argv=argv,
        version='pyzure-cli version 0.0.0'
    )

    if not args['<command>']:
        main(['--help'])
    else:
        pyzureCli = import_module('pyzure').main
        pyzureCli(
            args['<command>'] +
            ['--help']
        )
