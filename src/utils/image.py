from pathlib import Path
from ensure import ensure_annotations

import base64


@ensure_annotations
def decodeImage(imgstring: str, path: Path):
    img = base64.b64decode(imgstring)
    with open(path, 'wb') as f:
        f.write(img)
        f.close()

@ensure_annotations
def encodeImageIntoBase64(path: Path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read())
