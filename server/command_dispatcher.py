def _ignore_unrecognized_command(params=None):
    pass


class CommandDispatcher():
    def __init__(self, unrecognized_command_function=_ignore_unrecognized_command):
        """
        Initialize the class.
        :param unrecognized_command_function: The function to call for an unrecognized command
        """
        self._dispatcher = {}
        self._unrecognized = unrecognized_command_function

    def add_command(self, command, function):
        """
        Add the given command to the dispatcher.
        :param command: The command for which the function should be called.
        :param function: The function to call.
        """
        self._dispatcher[command] = function

    def dispatch_command(self, command, parameters=None):
        """
        Dispatch the given command.
        :param command: The command to call.
        :param parameters: The parameters to pass to the command's handling function.
        :return:
        """
        self._dispatcher.get(command, self._unrecognized)(parameters)
