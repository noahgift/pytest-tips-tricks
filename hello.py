""" this is the module docstring so the linter will not complain"""


def more_hello():
    """more hello function"""
    # import pdb;pdb.set_trace()
    return "hi"


def more_goodbye():
    """more goodbye function to test"""
    return "bye"


if __name__ == "__main__":
    more_hello()

# This is nonsense code that generates a warning
# var = 1
# var = var

# Bad syntax
# foo =
