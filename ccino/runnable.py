from __future__ import absolute_import


class Runnable(object):
    def __init__(self, func, parent, name=None):
        self._func = func
        self._parent = parent
        self._name = name or func.__name__

        self._skip = False

    def run(self, reporter, options):
        if not self.skipped and hasattr(self.func, '_skip') and \
                self.func._skip == True:
            self.skip()

    def skip(self):
        self._skip = True

    @property
    def func(self):
        return self._func

    @property
    def parent(self):
        return self._parent

    @property
    def name(self):
        return self._name

    @property
    def skipped(self):
        return self._skip
