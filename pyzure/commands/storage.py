"""
usage: pyzure storage [-h|--help] [<command> [<args>...]]

options:
    -h, --help
    
Commands to manage your Storage objects

storage account list [options]
    storage account (create|delete|check|set|show) [options] <name>

Commands to manage your Storage account keys
    storage account keys (list|renew) [options] <name>

Commands to show your Storage connection string
    storage account connectionstring show [options] <name>

Commands to manage your Storage containers
    storage container (create|delete|set|show) [options] [container]
    storage container list [options] [prefix]

Commands to manage shared access signatures of your Storage container
    storage container sas create [options] [container] [permissions] [expiry]

Commands to manage stored access policies of your Storage container
    storage container policy (create|delete|list|set|show) [options] [container] [name]

Commands to manage your Storage blobs
    storage blob list [options] [container] [prefix]
    storage blob (delete|show) [options] [container] [blob]
    storage blob upload [options] [file] [container] [blob]
    storage blob download [options] [container] [blob] [destination]

Commands to manage your blob copy operations
    storage blob copy start [options] [sourceUri] [destContainer]
    storage blob copy show [options] [container] [blob]
    storage blob copy stop [options] [container] [blob] [copyid]

Commands to manage shared access signature of your Storage blob
    storage blob sas create [options] [container] [blob] [permissions] [expiry]

Commands to manage your Storage file shares
    storage share (create|delete|set|show) [options] [share]
    storage share list [options] [prefix]

Commands to manage shared access signatures of your Storage file shares
    storage share sas create [options] [share] [permissions] [expiry]

Commands to manage stored access policies of your Storage file share
    storage share policy (create|delete|set|show) [options] [share] [name]
    storage share policy list [options] [share]

Commands to manage your Storage files
    storage file (delete|list) [options] [share] [path]
    storage file upload [options] [source] [share] [path]
    storage file download [options] [share] [path] [destination]

Commands to manage your file copy operations
    storage file copy start [options] [sourceUri] [destShare]
    storage file copy show [options] [share] [path]
    storage file copy stop [options] [share] [path] [copyid]

Commands to manage shared access signatures of your Storage file
    storage file sas create [options] [share] [path] [permissions] [expiry]

Commands to manage your Storage file directory
    storage directory (create|delete) [options] [share] [path]

Commands to manage your Storage queues
    storage queue (create|delete|show) [options] [queue]
    storage queue list [options] [prefix]

Commands to manage shared access signatures of your Storage queue
    storage queue sas create [options] [queue] [permissions] [expiry]

Commands to manage stored access policies of your Storage queue
    storage queue policy (create|delete|set|show)[options] [queue] [name]
    storage queue policy list [options] [queue]

Commands to manage your Storage logging properties
    storage logging (set|show) [options]

Commands to manage your Storage metrics properties
    storage metrics (set|show) [options]

Commands to manage your Storage CORS (Cross-Origin Resource Sharing)
    storage cors (delete|set|show) [options]

Commands to manage your Storage tables
    storage table (create|delete|show) [options] [table]
    storage table list [options] [prefix]

Commands to manage shared access signatures of your Storage table
    storage table sas create [options] [table] [permissions] [expiry]

Commands to manage stored access policies of your Storage table
    storage table policy (create|delete|set|show) [options] [table] [name]
    storage table policy list [options] [table]
"""

import sys
import os
from importlib import import_module
from docopt import docopt
from pprint import pprint as p

sys.path.append(os.path.join(os.path.dirname(__file__), "storage"))

commands = {command: import_module(command).main for command in [
    # 'account',
    # 'blob',
    'container',
    # 'cors',
    # 'directory',
    # 'file',
    # 'logging',
    # 'metrics',
    # 'queue',
    # 'share',
    # 'table
]}


def main(argv):

    args = docopt(
        __doc__,
        argv=argv,
        version='pyzure-cli version 0.0.0',
        options_first=True
    )

    command = args['<command>']

    if '<args>' in args.keys():
        argv = [command] + args['<args>']
    else:
        main(['--help'])

    if command in commands:
        commands[command](argv)
    else:
        main(['--help'])


if __name__ == '__main__':
    print(docopt(__doc__))
    main(sys.argv[1:])
