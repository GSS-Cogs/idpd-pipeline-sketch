"""
Functions to create nicely formatted and informative messages.
"""
from pathlib import Path

from deps.store.base import BaseWritableSingleDirectoryStore


# IMPORTANT - in all cases of a message  to us (rather than the external data provider)
# we'd want to inlcude a url pointing back to the airflown task thats failed.
# ... just not quite sure how to do that in a decoiupled way right now.

def unexpected_error(msg: str, error: Exception) -> str:
    """
    We've caught an unexpected error. Make a sensible message explaining
    the problem
    """
    return "some message"


def cant_create_config(pipeline, store, err: Exception) -> str:
    """
    Given the identifier for a pipeline and store (thus details of what files we have to work with)
    and the error we received on trying to create a config.

    Create some nicely formatted string message explaining what we got given and why
    we cant work out a pipeline config for it.
    """
    return "I am broke because...reasons"


def cant_find_scheama(config_dict, err: Exception) -> str:
    """
    We got an error when trying to identify the schema for the pipeline-conifg.json using the
    pipeline-config.json.

    Using the config-dict and the exceptioncreate a clear and informative message about what
    the problem is.
    """
    return "Some information about the problem"


def invalid_heuristically_created_config(config_dict, error: Exception) -> str:
    """
    We created a pipeline-config.json but its failing to validate.

    Provide suitable information so someone can find out why.
    """
    return "some message" 


def invlaid_config(config_dict, error: Exception) -> str:
    """
    The pipeline config that was provided is failing to validate.

    Provide suitable information so someone can find out why.
    """
    return "some message"
    

def subitter_notified(msg: str, config_dict: dict, error: Exception) -> str:
    """
    After we have nitified a data submitter of a problem we need to let ourselves
    know what has been communicated and to how.

    This should be a summation of what has been sent to which external party (so
    we are able to follow up if need be).
    """
    return "some message"


def unknown_pipeline(pipeline_name: str, config_dict: dict) -> str:
    """
    We've been given a pipeline identifier that we don't recnognise. Use the name of
    the runing pipeline and the pipeline configuration to rreate a meaningful message
    explaining the problem.
    """
    return "some message"


def pipeline_input_exception(pipeline_dict, store: BaseWritableSingleDirectoryStore, error: Exception):
    """
    Some pipeline details specifiy a file but there was an issue getting it out of the store.

    Given the pipeline_details dict, the store and the error encountered construct a sensible message that
    explains the problem.
    """
    return "some message"


def error_in_transform(pipeline_dict, store: BaseWritableSingleDirectoryStore, error: Exception) -> str:
    """
    An exception was raised during the transform process.

    Given the pipeline_details dict, the store and the error encountered construct a sensible message that
    explains the problem.
    """
    return "some message"

    
def pipeline_input_sanity_check_exception(pipeline_dict, store: BaseWritableSingleDirectoryStore, error: Exception) -> str:
    """
    
    """
    return "some message"


def metadata_validation_error(metadata_path, error: Exception) -> str:
    """
    The metadata has generated as validation error. Use the metadata and the error to create a
    sensible message explaining the problem.
    """
    return "some message"


def expected_file_submission_missing(msg: str, config_dict: dict, store: BaseWritableSingleDirectoryStore, pipeline_name: str = None) -> str:
    """
    The submission was missing a required file. Given the message, the config and the contents of the store
    return a suitable message.

    pipeline_name is optional as that's only appropriate where the message is
    intentended for internal (dissemination) eyes, so modify the message to include
    this only where pipeline_name is not None.
    """
    ...


def expected_local_file_missing(msg: str, file_path: Path, pipeline_name: str) -> str:
    """
    We're looking for a file on the local machine/runner nd cannot find it.

    Create a sensible message.

    _Ideally_ also provide a list of the file names that _do_ exist in the directory that
    we cannot find the required file in.
    """
    ...