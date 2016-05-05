from oem_framework.models.core import Model

import logging

log = logging.getLogger(__name__)


class Database(Model):
    def __init__(self, path, fmt, source, target):
        self.path = path
        self.format = fmt

        self.source = source
        self.target = target

        self.collections = {}

    def __repr__(self):
        return '<Database oem-%s-%s (%s)>' % (
            self.source,
            self.target,
            self.format.__extension__ if self.format else None
        )
