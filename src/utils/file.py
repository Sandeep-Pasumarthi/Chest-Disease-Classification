from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Union

import yaml
import os



@ensure_annotations
def read_yaml_file(path: Path) -> ConfigBox:
    with open(path, 'r') as f:
        return ConfigBox(yaml.safe_load(f))

@ensure_annotations
def write_yaml_file(path: Path, content: object, replace: bool = False) -> None:
    if replace:
        if os.path.exists(path):
            os.remove(path)
    
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        yaml.dump(content, f)
