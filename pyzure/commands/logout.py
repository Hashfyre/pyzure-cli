"""
usage: pyzure logout [options] [<name>]

options:
    -h, --help
    -v, --verbose             use verbose output
    -vv                       more verbose with debug output
    --json                    use json output
    -u,--username <username>  Required. User name used to log out from Azure Active Directory.

Log out from Azure subscription using Active Directory. Currently, the user can log out only via Microsoft organizational account
"""

import sys
from docopt import docopt


def main(argv):

    args = docopt(
        __doc__,
        argv=argv,
        version='pyzure-cli version 0.0.0'
    )

    sys.stdout.write("Stub for Azure logout {0}!".format(args['<name>']))
