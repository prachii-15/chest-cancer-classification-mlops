from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    data_dir: Path
    status_file: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_dir: Path
    image_size: list
    batch_size: int

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    trained_model_path: Path
    base_model: str
    params_epochs: int
    params_batch_size: int
    params_image_size: list