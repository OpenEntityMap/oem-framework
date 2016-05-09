from oem_framework.models.core import Model

import logging

log = logging.getLogger(__name__)


class Collection(Model):
    def __init__(self, storage, source, target, index=None, minify=None):
        self.storage = storage
        self.source = source
        self.target = target

        self.index = index
        self.minify = minify

    def get(self, key, hash=None, default=None):
        # Retrieve item
        item = self.index.get(key)

        if not item:
            return default

        # Match item (if `hash` provided)
        if hash is not None and item.hash != hash:
            return default

        return item

    def has(self, service, key, hash=None):
        return self.get(service, key, hash) is not None

    def set(self, key, metadata):
        if key is None:
            raise ValueError('Missing required parameter "key"')

        self.index[key] = metadata

    def __contains__(self, key):
        return key in self.index

    def __getitem__(self, key):
        return self.index[key]

    def __setitem__(self, key, value):
        self.index[key] = value

    def __repr__(self):
        if self.source and self.target:
            return '<Collection %s -> %s (%r)>' % (
                self.source,
                self.target,
                self.storage
            )

        return '<Collection %s (%r)>' % (
            self.source or self.target,
            self.storage
        )
