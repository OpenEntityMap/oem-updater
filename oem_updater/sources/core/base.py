import logging

log = logging.getLogger(__name__)


class Source(object):
    __key__ = None
    __parameters__ = []

    def __init__(self, collection, **kwargs):
        self.collection = collection
        self._kwargs = kwargs

    def run(self):
        raise NotImplementedError

    def param(self, name, default=None):
        return self._kwargs.get(
            '%s_%s' % (self.__key__, name),
            default
        )
