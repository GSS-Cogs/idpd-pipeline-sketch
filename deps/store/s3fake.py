from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

from .base import BaseWritableSingleDirectoryStore

# IMPORTANt !!!
# All code here is stubbed, these are hard coded returns of the sort
# of thing a real variation of BaseWritableSingleDirectoryStore would return.

# Note:
# a lot of these methods jave "lone" in the name, this just means
# it'd raise an error if more than one file is matched.
# just a sensible precaution when working with the idea of
# matching file names.

class FakeS3DirectoryStore(BaseWritableSingleDirectoryStore):
    """
    A fake/stubbed/hardcoded store class to represent what it'd be like to
    interact with a directory of files in this manner.
    """

    def __init__(self, pathlike: str):
        # Would probably just gather a list of paths to the files in
        # the directory in question
        ...
        
    def has_lone_file_matching(self, pattern: str) -> bool:
        """
        Checks is there's exactly one file in the directory with a name matching
        the provided regex.
        """
        return True
        
        
    def save_lone_file_matching(self, pattern: str) -> Path:
        """
        Asserts there's exactly one file in the directory matching the provided regex
        and saves it to the current working directory with its current filename,

        Raise an exception if a file of that name already exists in the
        current working directory.

        Returns a Path object to that location as a convenience.
        """
        ...
    
    def get_lone_matching_json_as_dict(self, pattern: str) -> dict:
        """
        Assert there's exactly one file matching the regex in the directory
        and attemptes to return it as a dictionary.

        This is a convenience to skip a dew steps if you just want to get
        the contents of a json file into a dict.
        """

        # hrd coded response for our exampkle
        if pattern == "pipeline-config.json":
            return {
                "schema": "airflow.schemas.ingress.sdmx.v1.schema.json",
                "required_files": [
                    {
                        "matches": "*.sdmx",
                        "count": 1 
                    }
                ],
                "supplementary_distributions": [
                    {
                        "matches": "*.sdmx",
                        "count": 1 
                    }
                ],
                "priority": 1,
                "contact": [
                  "jobloggs@ons.gov.uk"
                ],
                "pipeline": "default"
            }
        
        
    def get_file_names(self) -> List[str]:
        """
        Returns a list of names of all the files in the directory like store.
        """
        ...
        
    def get_current_source_pathlike(self) -> str:
        """
        Returns a string representing the path like structure to the directory we're working with

        Some examples:

        - s3://some-bucket-on-aws/dataset-cpih/23-01-2024T00:01:01/initial
        - /my-macbook/dataset-cpih/23-01-2024T00:01:01/initial
        """
        ...
    
    def add_file(self, file: Path):
        """
        Uploads/cuts/moves (depends on the type of store) the specified file
        to the directory this store represents.
        """
        ...