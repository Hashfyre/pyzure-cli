import logging
from cliff.command import Command

class storage(Command)
    "Azure top level command to manage Azure Storage Objects [ Table | Blob | File | Queue ]"

    log = logging.getLogger(__name__)

    self.LOG.debug('Runs storage commands')

    def prepare_to_run_command(self, cmd):
        self.LOG.debug('prepare_to_run_command %s', cmd.__class__.storage.__name__)

    def clean_up(self, cmd, result, err):
        self.LOG.debug('clean_up %s', cmd.__class__.storage.__name__)
        if err:
            self.LOG.debug('got an error: %s', err)
