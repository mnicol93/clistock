class CommandInvoker():
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def execute_command(self):
        if self._command:
            return self._command.execute()
