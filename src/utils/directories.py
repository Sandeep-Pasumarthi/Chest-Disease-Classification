from typing import List

import os


def create_directories(dir_paths: List[str]) -> None:
    for path in dir_paths:
        os.makedirs(path, exist_ok=True)
