from common_imports import *
from user_functions import get_user_id_from_code, assign_indices

# Test get_user_id_from_code function
def test_get_user_id_from_code_when_existing_user():
    # Arrange: Mock user_info dictionary
    user_info = {'user1': 101, 'user2': 102, 'user3': 103}
    code = 'user2'

    # Act: Call the get_user_id_from_code function
    result = get_user_id_from_code(user_info, code)

    # Assert: The result is the expected user ID
    assert result == 102

# Test get_user_id_from_code function with non-existing user
def test_get_user_id_from_code_when_non_existing_user():

    # Arrange: Mock user_info dictionary
    user_info = {'user1': 101, 'user2': 102, 'user3': 103}
    code = 'user4'

    # Act: Call the get_user_id_from_code function
    result = get_user_id_from_code(user_info, code)

    # Assert: The result is None
    assert result is None

# Test get_user_id_from_code function with print statement
def test_get_user_id_from_code_and_print_statement():

    # Redirect stdout to a StringIO object to capture print statements
    sys.stdout = StringIO()

    # Act: Call the get_user_id_from_code with non-existing user code
    get_user_id_from_code({'user1': 101}, 'user4')

    # Get the printed output
    printed_output = sys.stdout.getvalue()

    # Reset stdout
    sys.stdout = sys.__stdout__

    # Assert: The printed output contains the expected message
    assert printed_output.strip() == "No matching user found for code: user4"

# Test assign_indices function
def test_assign_indices_when_existing_user():

    # Arrange: Mock user_info dictionary
    user_info = {'user1': 101, 'user2': 102, 'user3': 103}

    # Act: Call the assign_indices function
    result = assign_indices(user_info)

    # Assert: The result is a dictionary with indices assigned to users
    assert result == {'user1': 0, 'user2': 1, 'user3': 2}

# Test assign_indices function with print statement
def test_assign_indices_and_print_statement():

    # Redirect stdout to a StringIO object to capture print statements
    sys.stdout = StringIO()

    # Call the function
    assign_indices({})

    # Get the printed output
    printed_output = sys.stdout.getvalue()

    # Reset stdout
    sys.stdout = sys.__stdout__

    # Assert: The printed output is empty
    assert printed_output.strip() == ""

# Test assign_indices function with Empty input
def test_assign_indices_when_empty_input():
    
    # Act: Call the function with an empty dictionary
    result = assign_indices({})

    # Assert: The result is also an empty dictionary
    assert result == {}

# Test assign_indices function with None input
def test_assign_indices_when_none_input():

    # Act: Call the function with None input
    result = assign_indices(None)

    # Assert: The result is also None
    assert result is None

# Test assign_indices function with no keys input
def test_assign_indices_when_no_keys_input():

    # Act: Call the function with a dictionary containing no keys
    result = assign_indices({})

    # Assert: The result is an empty dictionary
    assert result == {}