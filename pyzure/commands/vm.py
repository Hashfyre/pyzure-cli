
"""
usage: pyzure service [-h|--help] [<command>...]

options:
    -h, --help

Commands to manage your Virtual Machines

Create a VM
    vm create [options] <dns-name> <image> [userName] [password]

Create a VM from json role file
    vm create-from [options] <dns-name> <role-file>

List the VM
    vm list [options]

Show details about the VM
    vm show [options] <name>

Delete the VM
    vm delete [options] <name>

Start the VM
    vm start [options] <name>

Restart the VM
    vm restart [options] <name>

Shutdown the VM
    vm shutdown [options] <name>

Capture the VM as OS Image or VM Image
    vm capture [options] <vm-name> <target-image-name>

Export a VM to a file
    vm export [options] <vm-name> <file-path>

Commands to manage VM resource extensions
    vm extension list [options]
    vm extension set [options] <vm-name> <extension-name> <publisher-name> <version>
    vm extension set-chef [options] <vm-name>
    vm extension get [options] <vm-name>
    vm extension get-chef [options] <vm-name>

Commands to manage your Docker Virtual Machine
    vm docker create [options] <dns-name> <image> <user-name> [password]

Commands to manage your Virtual Machine locations
    vm location list [options]

Commands to manage your Virtual Machine static IP address
    vm static-ip show [options] <vm-name>
    vm static-ip set [options] <vm-name> <ip-address>
    vm static-ip remove [options] <vm-name>

Commands to manage your Virtual Machine public IP address
    vm public-ip list [options] [vm-name]
    vm public-ip set [options] [vm-name] [publicip-name]
    vm public-ip delete [options] [vm-name] [publicip-name]

Commands to manage your Virtual Machine endpoints
    vm endpoint create [options] <vm-name> <public-port> [local-port]
    vm endpoint create-multiple [options] <vm-name> <endpoints-config>
    vm endpoint delete [options] <vm-name> <endpoint-name>
    vm endpoint set [options] <vm-name> <endpoint-name>
    vm endpoint list [options] <vm-name>
    vm endpoint show [options] <vm-name> <endpoint-name>

Commands to manage your Virtual Machine endpoint's ACL rules
    vm endpoint acl-rule create [options] [vm-name] [endpoint-name] [order] [action] [remote-subnet]
    vm endpoint acl-rule list [options] [vm-name] [endpoint-name]
    vm endpoint acl-rule delete [options] [vm-name] [endpoint-name] [order]
    vm endpoint acl-rule set [options] [vm-name] [endpoint-name] [order]

Commands to manage your Virtual Machine images
    vm image show [options] <name>
    vm image list [options]
    vm image delete [options] <name>
    vm image create [options] <name> [source-path]

Commands to manage your Virtual Machine data disks
    vm disk show [options] <name>
    vm disk list [options] [vm-name]
    vm disk delete [options] <name>
    vm disk create [options] <name> [source-path]
    vm disk upload [options] <source-path> <blob-url> <storage-account-key>
    vm disk attach [options] <vm-name> <disk-image-name>
    vm disk attach-new [options] <vm-name> <size-in-gb> [blob-url]
    vm disk detach [options] <vm-name> <lun>
    vm disk update [options] <vm-name> <lun>
"""

import sys
from importlib import import_module
from docopt import docopt

sys.path.append('./vm')
commands = {command: import_module(command).main for command in [
    'create',
    'create-from',
    'list',
    'show',
    'delete',
    'start',
    'restart',
    'shutdown',
    'capture',
    'export',
    'extension',
    'docker',
    'location',
    'static-ip',
    'public-ip',
    'endpoint',
    'image',
    'disk'    
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
