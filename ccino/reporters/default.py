from __future__ import absolute_import

from .base import BaseReporter, CHECK_SYMBOL, override


class DefaultReporter(BaseReporter):
    """Default ccino reporter.

    This is essentially a mirror of the 'spec' reporter on Mocha. It
    provides a clear hierarchy for the suites and tests as they are
    displayed.
    """

    @override
    def start(self):
        self.write('\n')

    @override
    def suite_start(self, suite):
        if not suite.name == 'root':
            self.write('  ' * self.num_open_suites + suite.name + '\n')

    @override
    def test_pass(self, test):
        padding = '  ' * (self.num_open_suites + 1)
        check = self.terminal.green(CHECK_SYMBOL)
        desc = self.terminal.bright_black(test.desc)

        message = padding + check + ' ' + desc + '\n'

        self.write(message)

    @override
    def test_fail(self, test):
        padding = '  ' * (self.num_open_suites + 1)
        number = self.terminal.red('{:d})'.format(self.num_failures - 1))
        desc = self.terminal.red(test.desc)

        self.write(padding + number + ' ' + desc + '\n')

    @override
    def test_pending(self, test):
        padding = '  ' * (self.num_open_suites + 1)
        desc = self.terminal.cyan('- ' + test.desc)

        message = padding + desc + '\n'

        self.write(message)

    @override
    def hook_fail(self, hook):
        padding = '  ' * (self.num_open_suites + 1)
        number = self.terminal.red('{:d})'.format(self.num_failures - 1))
        desc = self.terminal.red(hook.desc)

        self.write(padding + number + ' ' + desc + '\n')

    @override
    def end(self, time):
        self.write('\n')
        self.print_summary()
        self.write('\n')
