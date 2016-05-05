from oem_framework.models.core import Model


class Metadata(Model):
    __slots__ = ['collection', 'key', 'revision', 'hashes', 'media']

    def __init__(self, collection, key, revision=0, hashes=None, media=None):
        self.collection = collection
        self.key = key

        self.revision = revision
        self.hashes = hashes or {}

        self.media = media

    @property
    def index(self):
        return self.collection.index

    def to_dict(self):
        return {
            'revision': self.revision,
            'hashes': self.hashes,

            'media': self.media
        }

    @classmethod
    def from_dict(cls, collection, data, key=None):
        return cls(
            collection, key,
            data.get('revision'),
            data.get('hashes'),
            data.get('media')
        )
