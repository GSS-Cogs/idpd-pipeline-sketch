from pathlib import Path

def smdx_default_v1(sdmx_file: Path):
    """
    A fake transform
    """
    return Path("data.csv"), Path("metadata.json")
    

def sdmx_sanity_check_v1(sdmx_file: Path):
    """
    A fake sdmx sanith check.

    Basically a a super light touch that'll raises an errror if
    the sibmitted "sdmx" is obviously silly/wrong/not-an-sdmx-file.
    """