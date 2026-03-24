import yaml
from pathlib import Path
from src.chest_cancer.entity.config_entity import DataIngestionConfig
from src.chest_cancer.entity.config_entity import DataValidationConfig
from src.chest_cancer.entity.config_entity import DataTransformationConfig
from src.chest_cancer.entity.config_entity import ModelTrainerConfig

class ConfigurationManager:

    def __init__(self, config_filepath="config/config.yaml", params_filepath="params.yaml"):
        with open(config_filepath) as yaml_file:
            self.config = yaml.safe_load(yaml_file)
        
        with open(params_filepath) as yaml_file:
            self.params = yaml.safe_load(yaml_file)

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
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config["model_trainer"]
        params = self.params

        root_dir = Path(config["root_dir"])
        root_dir.mkdir(parents=True, exist_ok=True)

        model_trainer_config = ModelTrainerConfig(
            root_dir=root_dir,
            trained_model_path=Path(config["trained_model_path"]),
            base_model=config["base_model"],
            params_epochs=params["EPOCHS"],
            params_batch_size=params["BATCH_SIZE"],
            params_image_size=params["IMAGE_SIZE"]
        )

        return model_trainer_config