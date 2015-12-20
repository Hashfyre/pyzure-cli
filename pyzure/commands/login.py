"""
usage: pyzure login [options] [<name>]

options:
    -h, --help
    -v, --verbose                   use verbose output
    -vv                             more verbose with debug output
    --json                          use json output
    -u --username <username>        user name or service principal ID. If multifactor authentication is required, you will be prompted to use the login command without parameters for interactive support.
    -e --environment [environment]  Environment to authenticate against, such as AzureChinaCloud; must support active directory.
    -p --password <password>        user password or service principal key, will prompt if not given.
    --service-principal             If given, log in as a service principal rather than a user.
    --tenant <tenant>               Tenant domain or ID to log into.
    -q --quiet                      do not prompt for confirmation of PII storage.

Log in to an Azure subscription using Active Directory or a Microsoft account identity.

"""

import sys
from docopt import docopt


def main(argv):

    args = docopt(
        __doc__,
        argv=argv,
        version='pyzure-cli version 0.0.0'
    )

    sys.stdout.write("Stub for Azure login {0}!".format(args['<name>']))
