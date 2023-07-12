import os
from src.configHelpers import *


def test_read_config():
    # Create a temporary configuration file
    with open('test_config.json', 'w') as f:
        f.write('[{"name": "config1"}, {"name": "config2"}]')

    # Test reading the configuration file
    result = readConfig("test_config.json", toClass=False)

    # Verify the result
    assert result == [{'name': 'config1'}, {'name': 'config2'}]

    # Remove the temporary configuration file
    os.remove('test_config.json')


def test_read_config_with_class():
    # Create a temporary configuration file
    with open('test_config.json', 'w') as f:
        f.write('[{"name": "config1"}, {"name": "config2"}]')

    # Test reading the configuration file
    result = readConfig("test_config.json")

    # Verify the result
    assert result[0].name == 'config1'

    # Remove the temporary configuration file
    os.remove('test_config.json')
