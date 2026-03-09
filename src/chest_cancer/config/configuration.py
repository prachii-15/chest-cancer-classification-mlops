import yaml
from pathlib import Path
from src.chest_cancer.entity.config_entity import DataIngestionConfig
from src.chest_cancer.entity.config_entity import DataValidationConfig
from src.chest_cancer.entity.config_entity import DataTransformationConfig

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
    
    def get_data_validation_config(self):
        config = self.config["data_validation"]

        data_validation_config = DataValidationConfig(
            root_dir = Path(config["root_dir"]),            
            data_dir = Path(config["data_dir"]),           
            status_file = Path(config["status_file"])            
        )

        return data_validation_config

    def get_data_transformation_config(self):
        config = self.config["data_transformation"]

        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config["root_dir"]),
            data_dir=Path(config["data_dir"]),
            image_size=config["image_size"],
            batch_size=config["batch_size"]
        )

        return data_transformation_config