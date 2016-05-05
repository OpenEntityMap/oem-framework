from oem_framework.models.core import Model, ModelRegistry

import logging
import os

log = logging.getLogger(__name__)


class Index(Model):
    def __init__(self, collection, path, fmt, items=None):
        self.collection = collection
        self.path = path
        self.format = fmt

        self.items = items or {}
        self.items_path = os.path.join(os.path.dirname(path), 'items')

    @classmethod
    def from_dict(cls, collection, data, path=None, fmt=None, **kwargs):
        index = cls(collection, path, fmt)

        if 'items' not in data:
            return index

        # Parse items
        index.items = dict([
            (key, ModelRegistry['Metadata'].from_dict(collection, value, key))
            for key, value in data['items'].items()
        ])

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
        try:
            return self.items[str(key)]
        except KeyError:
            return self.items[key]

    def __setitem__(self, key, value):
        self.items[str(key)] = value

    def __repr__(self):
        source = self.collection.source
        target = self.collection.target

        if source and target:
            return '<Index %s -> %s (%s)>' % (
                source,
                target,
                self.format.extension if self.format else None
            )

        return '<Index %s (%s)>' % (
            source or target,
            self.format.extension if self.format else None
        )
