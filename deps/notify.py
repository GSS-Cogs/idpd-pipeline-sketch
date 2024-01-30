import json

# TODO - these messages should be more complex and should
# include template strings for common issues (particularly where
# we're sending an email.

def publishing_support(msg: str):
    """
    Send a messge to a channel or avaenue of contact such that it reaches the
    publishing support team.
    """
    ...


def data_engineering(msg: str):
    """
    Send a messge to a channel or avaenue of contact such that it reaches the
    data engineers.
    """
    ...

# IMPORTANT - where we're notifying the SEs we also want to nitify the DEs so they
# know there's a software issues that's being looked into.
def software_engineering(msg: str):
    """
    Send a messge to a channel or avaenue of contact such that it reaches the
    software engineers.
    """
    ...

def data_submmitter_of_validation_error(msg: str, error: Exception):
    """
    Send a messge to a channel or avaenue of contact such that it reaches the
    registred contact email the data was submitted with. Include information on
    a specific json schema validation error.
    """
    # Turn a ValidationError and a message into something that'll be easy to
    # read in the form of an email.
    ...