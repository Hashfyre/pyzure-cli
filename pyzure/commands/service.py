
"""
usage: pyzure service [-h|--help] [<command>...]

options:
    -h, --help

Commands to manage your Cloud Services

Create a cloud service
    service create [options] <serviceName>

List Azure cloud services
    service list [options]

Show Azure cloud service
    service show [options] <serviceName>

Delete a cloud service
    service delete [options] <serviceName>

Get details of deployment events.
    service get-deployment-event [options] <serviceName> <startTime> <endTime>

Commands to manage your Cloud Services certificates
    service cert list [options]
    service cert create [options] <dns-name> <file> [password]
    service cert delete [options] <thumbprint>

Commands to manage internal load balancers for your Cloud Service Deployment
    service internal-load-balancer list [options] [serviceName]
    service internal-load-balancer add [options] [serviceName] [internalLBName]
    service internal-load-balancer delete [options] [serviceName] [internalLBName]
    service internal-load-balancer set [options] [serviceName] [internalLBName]

Commands to manage load balanced set for a Cloud Service Deployment
    service load-balanced-set list [options] <serviceName>
    service load-balanced-set show [options] <serviceName>
    service load-balanced-set set [options] <serviceName> <load-balanced-set-name>
"""

import sys
from importlib import import_module
from docopt import docopt

sys.path.append('./service')
commands = {command: import_module(command).main for command in [
    'create',
    'list',
    'show',
    'delete',
    'get-deployment-event',
    'cert',
    'internal-load-balancer',
    'load-balanced-set'
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
