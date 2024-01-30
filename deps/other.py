from pathlib import Path
from typing import Tuple

from .store.base import BaseWritableSingleDirectoryStore
from .store.s3fake import FakeS3DirectoryStore

def directory_store_from_pathlike_source(pathlike: str):
    """
    Given a pathlike string that indicates a directory like structure
    returns a directory like store, the type of directory like
    store would depend on the pathlike

    i.e:
    s3://an-aws-bucket/stuff/ - an S3 directory store
    gs://a-gcp-sbucket/things/ - a gcp storage ditectory store
    /stuff/things - a local directory store
    """
    return FakeS3DirectoryStore(pathlike)


def schema_path_from_config(config: dict) -> dict:
    """
    Given a config, work out and return the json schema that is used to enforce
    that config.
    """
    ...


def heuristically_create_pipeline_config(store: BaseWritableSingleDirectoryStore):
    """
    Given access to a directory store, guess the pipeline-config.json we
    should be using.
    """
    ...


def validate_json(*args, **kwargs):
    """
    Validate the schema
    """
    ...


def smdx_default_v1(*args, **kwargs) -> Tuple[Path, Path]:
    """
    A fake transform.
    """
    return Path("data.csv"), Path("metadata.json")


def sdmx_sanity_check_v1(*args, **kwargs):
    """
    A fake sdmx sanity checking function
    """
    ...


def get_pipeline_identifier_from_config(pipeline_config: dict) -> str:
    """
    Given the contents of a pipeline-config.json returns the name
    for the pipeline to be ran.

    i.e in the v2 schema the contents of the "pipeline" field.
    """
    return "sdmx.default"
    

class UploadServiceClient:
    """
    A client for uploading files to the upload service
    """

    def upload(self, file_path: Path):
        ...

def get_supplementary_distribution_patterns(config_dict):
    """
    Given the contents of pipeline-config.json as a dictionary,
    return the regex patterns that identify the supplementary
    distributions to be uploaded alongisde the csv.
    """
    return ["*.sdmx"]

def get_required_file_patterns(config_dict):
    """
    Given the contents of pipeline-config.json as a dictionary,
    return the regex patterns that identify the required
    files for the transform.
    """
    return ["*.sdmx"]

class DatasetApiClient:
    """
    An entirely fake dataset api metadata upload client
    """

    def upload(self, stuff):
        ...

def validate_csv(csv_path: Path, metadata_path: Path):
    """
    Validate a csv
    """
    ...
    