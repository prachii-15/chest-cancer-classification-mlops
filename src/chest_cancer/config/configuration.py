import yaml
from pathlib import Path
from src.chest_cancer.entity.config_entity import DataIngestionConfig

class ConfigurationManager:

    def __init__(self, config_filepath="config/config.yaml"):
        with open(config_filepath) as yaml_file:
            self.config = yaml.safe_load(yaml_file)

    def get_data_ingestion_config(self):

        config = self.config["data_ingestion"]

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config["root_dir"]),
            source_dir=Path(config["source_dir"])
        )

        return data_ingestion_config