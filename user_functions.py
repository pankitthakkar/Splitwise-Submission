# Gets the ID from the code in the excel file
# Example: "A": "12345678"
# It will get the ID 12345678 from the code A
def get_user_id_from_code(user_info, code):
    if code in user_info:
        return user_info[code]
    else:
        print(f"No matching user found for code: {code}")
        return None

# Assigns indices to the users
# Requirements from the Splitwise API (https://dev.splitwise.com/#tag/expenses/paths/~1create_expense/post)
def assign_indices(user_info):
    if user_info is None:
        return None
    # Sort the user codes alphabetically
    sorted_users = sorted(user_info.keys())
    # Create a dictionary to store the assigned indices
    user_indices = {}
    # Assign indices to the users based on their alphabetical order
    for index, code in enumerate(sorted_users):
        user_indices[code] = index
    return user_indices