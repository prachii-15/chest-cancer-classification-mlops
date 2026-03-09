from src.chest_cancer.config.configuration import ConfigurationManager
from src.chest_cancer.components.data_ingestion import DataIngestion

class TrainingPipeline:
    def start_data_ingestion(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.copy_dataset()