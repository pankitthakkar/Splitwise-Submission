from common_imports import *
from config import load_config

# Define the path to the test JSON configuration file
TEST_JSON_FILE = 'test_config.json'

# Define test data
TEST_CONFIG_DATA = {
    "bearer_token": "123beartoken456",
    "groups": [
        {
            "group_id": "12groupid34",
            "group_name": "GroupName",
            "user_info": {
                "A": "12345678",
                "B": "23456789",
                "C": "34567890",
                "D": "45678901",
                "E": "56789012",
                "F": "67890123",
                "G": "78901234"
            }
        }
    ]
}

# File is a valid JSON file
def test_load_config_when_valid_file():

    # Arrange: Write the test JSON data to a file
    with open(TEST_JSON_FILE, 'w') as f:
        json.dump(TEST_CONFIG_DATA, f)

    # Act: Call the load_config function
    config = load_config(TEST_JSON_FILE)

    # Assert: Loaded configuration matches the test data
    assert config == TEST_CONFIG_DATA

    # Clean up: Delete the test JSON file after the test
    os.remove(TEST_JSON_FILE)

# File does not exist
def test_load_config_throw_FileNotFoundError_when_non_existent_file():

    # Assert: Loading a non-existent file raises a FileNotFoundError
    with pytest.raises(FileNotFoundError):
        load_config('non_existent_file.json')

# JSON data is invalid
def test_load_config_invalid_json():
    # Arrange: Write invalid JSON data to a file
    with open(TEST_JSON_FILE, 'w') as f:
        f.write('invalid_json_data')

    # Assert: Loading the config raises a JSONDecodeError
    with pytest.raises(json.JSONDecodeError):
        load_config(TEST_JSON_FILE)

    # Clean up: delete the test JSON file after the test
    os.remove(TEST_JSON_FILE)

# JSON data is empty
def test_load_config_when_empty_json_file():
    # Arrange: Write an empty JSON file
    with open(TEST_JSON_FILE, 'w') as f:
        f.write('{}')

    # Act: Call the load_config function
    config = load_config(TEST_JSON_FILE)

    # Assert: The loaded configuration is an empty dictionary
    assert config == {}

    # Clean up: Delete the test JSON file after the test
    os.remove(TEST_JSON_FILE)

# JSON data contains incorrect structure
def test_load_config_incorrect_structure():
    # Arrange: Write a JSON file with incorrect structure
    with open(TEST_JSON_FILE, 'w') as f:
        f.write('{"missing_key": "value"}')

    # Act: Call the load_config function
    config = load_config(TEST_JSON_FILE)

    # Assert: The loaded configuration should not be None
    assert config is not None

    # Clean up: delete the test JSON file after the test
    os.remove(TEST_JSON_FILE)

# JSON data contains unexpected keys
def test_load_config_when_unexpected_keys():
    # Arrange: Write a JSON file with unexpected keys
    with open(TEST_JSON_FILE, 'w') as f:
        json.dump({"unexpected_key": "value"}, f)

    # Act: Call the load_config function
    config = load_config(TEST_JSON_FILE)

    # Assert: The loaded configuration does not contain unexpected keys
    assert "unexpected_key" not in config.values()

    # Clean up: delete the test JSON file after the test
    os.remove(TEST_JSON_FILE)
