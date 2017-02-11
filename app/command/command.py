from flask_script import Command, Option
from abc import abstractmethod
from flask_script import Manager


class CommandBase(Command):
    def __init__(self, *args, **kwargs):
        super(CommandBase, self).__init__(*args, **kwargs)

        self.options = {}

    def run(self, **kwargs):
        self.options = kwargs

        return self._run()

    @abstractmethod
    def _run(self):
        pass

    def get_option(self, key, default=None):
        return self.options.get(key, default)

    @staticmethod
    def p(message):
        print message.encode('utf8')


class CustomCommand(CommandBase):
    @abstractmethod
    def _run(self):
        pass

    def get_options(self):
        return [
            Option('--version', dest='name', default='v1', help='api version')
        ]


class _CustomManger(Manager):
    """

    """
CustomMangerService = _CustomManger()


class PrintArgsService(CustomCommand):
    def _run(self):
        version = self.get_option('name')
        print version

CustomMangerService.add_command("test", PrintArgsService())