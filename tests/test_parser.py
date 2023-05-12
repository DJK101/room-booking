import pytest
import app.commands as commands
from app.parser import parse_command


@pytest.mark.parametrize("function_name, command", [('help_menu', 'help')])
def test_parse_command_to_call_command(mocker, function_name, command):
    command_function = mocker.spy(commands, function_name)
    parse_command(command)
    assert command_function.call_count == 1
