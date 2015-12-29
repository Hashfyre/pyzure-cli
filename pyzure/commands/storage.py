"""
usage: pyzure storage [-h|--help] [<command>...]

options:
    -h, --help

Commands to manage your Storage objects

storage account list [options]
    storage account show [options] <name>
    storage account create [options] <name>
    storage account set [options] <name>
    storage account delete [options] <name>
    storage account check [options] <name>

Commands to manage your Storage account keys
    storage account keys list [options] <name>
    storage account keys renew [options] <name>

Commands to show your Storage connection string
    storage account connectionstring show [options] <name>

Commands to manage your Storage containers
    storage container list [options] [prefix]
    storage container show [options] [container]
    storage container create [options] [container]
    storage container delete [options] [container]
    storage container set [options] [container]

Commands to manage shared access signatures of your Storage container
    storage container sas create [options] [container] [permissions] [expiry]

Commands to manage stored access policies of your Storage container
    storage container policy create [options] [container] [name]
    storage container policy show [options] [container] [name]
    storage container policy list [options] [container]
    storage container policy set [options] [container] [name]
    storage container policy delete [options] [container] [name]

Commands to manage your Storage blobs
    storage blob list [options] [container] [prefix]
    storage blob show [options] [container] [blob]
    storage blob delete [options] [container] [blob]
    storage blob upload [options] [file] [container] [blob]
    storage blob download [options] [container] [blob] [destination]

Commands to manage your blob copy operations
    storage blob copy start [options] [sourceUri] [destContainer]
    storage blob copy show [options] [container] [blob]
    storage blob copy stop [options] [container] [blob] [copyid]

Commands to manage shared access signature of your Storage blob
    storage blob sas create [options] [container] [blob] [permissions] [expiry]

Commands to manage your Storage file shares
    storage share create [options] [share]
    storage share show [options] [share]
    storage share set [options] [share]
    storage share delete [options] [share]
    storage share list [options] [prefix]

Commands to manage shared access signatures of your Storage file shares
    storage share sas create [options] [share] [permissions] [expiry]

Commands to manage stored access policies of your Storage file share
    storage share policy create [options] [share] [name]
    storage share policy show [options] [share] [name]
    storage share policy list [options] [share]
    storage share policy set [options] [share] [name]
    storage share policy delete [options] [share] [name]

Commands to manage your Storage files
    storage file list [options] [share] [path]
    storage file delete [options] [share] [path]
    storage file upload [options] [source] [share] [path]
    storage file download [options] [share] [path] [destination]

Commands to manage your file copy operations
    storage file copy start [options] [sourceUri] [destShare]
    storage file copy show [options] [share] [path]
    storage file copy stop [options] [share] [path] [copyid]

Commands to manage shared access signatures of your Storage file
    storage file sas create [options] [share] [path] [permissions] [expiry]

Commands to manage your Storage file directory
    storage directory create [options] [share] [path]
    storage directory delete [options] [share] [path]

Commands to manage your Storage queues
    storage queue create [options] [queue]
    storage queue list [options] [prefix]
    storage queue show [options] [queue]
    storage queue delete [options] [queue]

Commands to manage shared access signatures of your Storage queue
    storage queue sas create [options] [queue] [permissions] [expiry]

Commands to manage stored access policies of your Storage queue
    storage queue policy create [options] [queue] [name]
    storage queue policy show [options] [queue] [name]
    storage queue policy list [options] [queue]
    storage queue policy set [options] [queue] [name]
    storage queue policy delete [options] [queue] [name]

Commands to manage your Storage logging properties
    storage logging show [options]
    storage logging set [options]

Commands to manage your Storage metrics properties
    storage metrics show [options]
    storage metrics set [options]

Commands to manage your Storage CORS (Cross-Origin Resource Sharing)
    storage cors set [options]
    storage cors show [options]
    storage cors delete [options]

Commands to manage your Storage tables
    storage table create [options] [table]
    storage table list [options] [prefix]
    storage table show [options] [table]
    storage table delete [options] [table]

Commands to manage shared access signatures of your Storage table
    storage table sas create [options] [table] [permissions] [expiry]

Commands to manage stored access policies of your Storage table
    storage table policy create [options] [table] [name]
    storage table policy show [options] [table] [name]
    storage table policy list [options] [table]
    storage table policy set [options] [table] [name]
    storage table policy delete [options] [table] [name]
"""

import sys
import os
from importlib import import_module
from docopt import docopt

# sys.path.append('/storage')
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
        version='pyzure-cli version 0.0.0'
        # options_first=True
    )

    command = args['<command>']
    argv = [command] + args['<args>']
    if command in commands:
        commands[command](argv)
    else:
        main(['--help'])


if __name__ == '__main__':
    main(sys.argv[1:])
