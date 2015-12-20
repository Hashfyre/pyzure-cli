"""
usage: pyzure account [-h|--help] [<command>...]

options:
    -h, --help

Commands to manage your account information and publish settings

List the imported subscriptions
    account list [options]

Show details about a subscription
    account show [options] [subscriptionNameOrId]

Set the current subscription
    account set [options] <subscriptionNameOrId>

Remove a subscription or environment, or clear all of the stored account and environment info
    account clear [options]

Import a publishsettings file or certificate for your account
    account import [options] <file>

Launch a browser to download your publishsettings file
    account download [options]

Commands to manage your account environment
    account env list [options]
    account env show [options] [environment]
    account env add [options] [environment]
    account env set [options] [environment]
    account env delete [options] [environment]

Commands to manage your Affinity Groups
    account affinity-group list [options]
    account affinity-group create [options] <name>
    account affinity-group show [options] <name>
    account affinity-group delete [options] <name>

Commands to manage your account certificates
    account cert export [options]
"""

import sys
from importlib import import_module
from docopt import docopt

sys.path.append('./account')
commands = {command: import_module(command).main for command in [
    'list',
    'show',
    'set',
    'clear',
    'import',
    'download',
    'env',
    'affinity-group',
    'cert'
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
