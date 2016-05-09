from oem_framework.models.core import Model

import logging
import sys

log = logging.getLogger(__name__)


class Index(Model):
    def __init__(self, collection, storage, items=None):
        self.collection = collection
        self.storage = storage

        self.items = items or {}

    @classmethod
    def from_dict(cls, collection, data, storage=None, **kwargs):
        index = cls(collection, storage)

        # Update index with items
        if 'items' in data:
            index.items = data['items']

        return index

    def to_dict(self):
        return {
            'items': dict([
                (key, item.to_dict())
                for key, item in self.items.items()
            ])
        }

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return str(key) in self.items or key in self.items

    def __getitem__(self, key):
        # Retrieve item
        try:
            value = self.items[str(key)]
        except KeyError:
            exc_info = sys.exc_info()

            try:
                value = self.items[key]
            except KeyError:
                raise exc_info[0], exc_info[1], exc_info[2]

        # Ensure item has been parsed
        if type(value) is dict:
            value = self.items[str(key)] = self.storage.parse_metadata(self.collection, key, value)

        return value

    def __setitem__(self, key, value):
        self.items[str(key)] = value

    def __repr__(self):
        source = self.collection.source
        target = self.collection.target

        if source and target:
            return '<Index %s -> %s (%r)>' % (
                source,
                target,
                self.storage
            )

        return '<Index %s (%r)>' % (
            source or target,
            self.storage
        )
