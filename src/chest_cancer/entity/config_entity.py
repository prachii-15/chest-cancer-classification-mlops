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