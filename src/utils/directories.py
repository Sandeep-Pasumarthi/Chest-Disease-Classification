from ensure import ensure_annotations
from typing import List
from pathlib import Path

import os


def create_directories(dir_paths: List[Path]) -> None:
    for path in dir_paths:
        os.makedirs(path, exist_ok=True)
