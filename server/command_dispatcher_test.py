import command_dispatcher
import unittest


class CommandParserTests(unittest.TestCase):
    def test_calls_proper_command_function(self):
        function_called = False

        def function(params=None):
            nonlocal function_called
            function_called = True

        parser = command_dispatcher.CommandDispatcher()
        parser.add_command('test', function)

        parser.dispatch_command('test')

        self.assertTrue(function_called)

    def test_calls_ignored_function_for_invalid_command(self):
        function_called = False
        ignore_called = False

        def function(params=None):
            nonlocal function_called
            function_called = True

        def ignore(params=None):
            nonlocal ignore_called
            ignore_called = True

        parser = command_dispatcher.CommandDispatcher(unrecognized_command_function=ignore)
        parser.add_command('test', function)

        parser.dispatch_command('asdf')

        self.assertFalse(function_called)
        self.assertTrue(ignore_called)

    def test_passes_parameters_to_function(self):
        parameters = None

        def function(params):
            nonlocal parameters
            parameters = params

        parser = command_dispatcher.CommandDispatcher()
        parser.add_command('test', function)

        parser.dispatch_command('test', 'params')

        self.assertEqual(parameters, 'params')


if __name__ == '__main__':
    unittest.main()
