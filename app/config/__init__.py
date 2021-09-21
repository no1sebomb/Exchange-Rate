# coding=utf-8

import json
import typing as t
from pathlib import Path


def load_json(filename: str, dirpath: Path = Path(__file__).resolve().parent) -> t.Dict[str, t.Any]:
    """
    Loading JSON-formatted file

    Args:
        filename (str): Name of file you want to load (without .json extension)
        dirpath (Path): File directory path
    Returns:
        t.Dict[str, t.Any]: Loaded JSON data
    """

    with (dirpath / "{}.json".format(filename)).open("rt", encoding="utf-8") as jsonFile:
        return json.load(jsonFile)


CONFIG = load_json("config.json")


__all__ = ("CONFIG", )
