from oem_framework.storage.core.base import BaseStorage


class ProviderStorage(BaseStorage):
    @classmethod
    def open(cls, client, path=None):
        """
        :rtype: ProviderStorage
        """
        raise NotImplementedError

    #
    # Provider methods
    #

    def create(self, source, target):
        """
        :rtype: bool
        """
        raise NotImplementedError

    def open_database(self, source, target, version=None):
        """
        :rtype: oem_framework.models.Database
        """
        raise NotImplementedError

    #
    # Index methods
    #

    def has_index(self, source, target, version):
        """
        :rtype: bool
        """
        raise NotImplementedError

    def update_index(self, source, target, version, response):
        """
        :rtype: bool
        """
        raise NotImplementedError

    #
    # Item methods
    #

    def has_item(self, source, target, version, key):
        """
        :rtype: bool
        """
        raise NotImplementedError

    def update_item(self, source, target, version, key, response, metadata):
        """
        :rtype: bool
        """
        raise NotImplementedError
