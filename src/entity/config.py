from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class LoadModelConfig:
    root_dir: Path
    model_path: Path
    image_size: list
    learning_rate: float
    include_top: bool
    weights: str
    classes: int

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    base_model_path: Path
    trained_model_path: Path
    training_data: Path
    epochs: int
    batch_size: int
    patience: int
    agumentation: bool
    image_size: list
