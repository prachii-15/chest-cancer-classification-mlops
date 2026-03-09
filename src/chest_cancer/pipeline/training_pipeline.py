from src.chest_cancer.config.configuration import ConfigurationManager
from src.chest_cancer.components.data_ingestion import DataIngestion
from src.chest_cancer.components.data_validation import DataValidation

class TrainingPipeline:
    def start_data_ingestion(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.copy_dataset()

    def start_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_dataset()