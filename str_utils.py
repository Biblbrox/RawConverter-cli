import os
import glob


def parse_path(filename):
    """
    Parse Unix-style file name.
    Returns list of files
    :return []
    """

    """
    :type filename: str
    """
    if '*' in filename:
        filename = glob.glob(filename)
        return filename

    return [filename]


def get_files(dir_name):
    """
    Return list of files in dir_name
    :param dir_name:
    :return: []
    """
    if not os.path.exists(dir_name):
        raise FileNotFoundError(
            f"Directory {dir_name} not found or not granted permission")
    return [file for file in os.listdir(dir_name) if os.path.isfile(file)]


__all__ = [
    "get_files", "parse_path"
]
