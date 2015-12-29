#! /usr/bin/env python
"""
usage: pyzure [-h|--help] [-v|--version] [<command> [<args>...]]

options:
    -h, --help
    -v, --version
    
commands:
    login       Command to login into your Windows Azure account
    logout      Command to logout of your Windows Azure account
    account     Commands to manage your account information and publish settings
    config      Commands to manage your local settings
    network     Commands to manage your networks
    service     Commands to manage your Cloud Services
    storage     Commands to manage your Storage objects
    vm          Commands to manage your Virtual Machines
"""
# planned commands in v 0.2.0 (that exist in azure-cli nodejs cli-tool)
#    hdinsight   Commands to manage HDInsight clusters and jobs
#    mobile      Commands to manage your Mobile Services

#    sb          Commands to manage your Service Bus configuration
#    site        Commands to manage your Web Sites
#    sql         Commands to manage your SQL Server accounts


import sys
import os
from importlib import import_module
from docopt import docopt

sys.path.append(os.path.join(os.path.dirname(__file__), "commands"))

commands = {command: import_module(command).main for command in [
    'help',
    'hullo',
    # 'login',
    # 'logout',
    # 'account',
    # 'config',
    # 'network',
    # 'service',
    'storage',
    # 'vm'
]}


def main(argv):

    args = docopt(
        __doc__,
        argv=argv,
        version='pyzure-cli version 0.0.0',
        options_first=True
    )

    command = args['<command>']
    argv = [command] + args['<args>']
    if command in commands:
        commands[command](argv)
    else:
        main(['--help'])


if __name__ == '__main__':
    main(sys.argv[1:])
