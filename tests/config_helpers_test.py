import os
from src.configHelpers import readConfig

def test_readConfig():
    # Create a temporary configuration file
    with open('test_config.json', 'w') as f:
        f.write('[{"name": "config1"}, {"name": "config2"}]')

    # Test reading the configuration file
    result = readConfig()

    # Verify the result
    assert result == [{'name': 'config1'}, {'name': 'config2'}]

    # Remove the temporary configuration file
    os.remove('test_config.json')