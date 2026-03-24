from src.chest_cancer.config.configuration import ConfigurationManager
from src.chest_cancer.components.data_ingestion import DataIngestion
from src.chest_cancer.components.data_validation import DataValidation
from src.chest_cancer.components.data_transformation import DataTransformation
from src.chest_cancer.components.model_trainer import ModelTrainer

class TrainingPipeline:
    def __init__(self):
        self.config = ConfigurationManager()

        self.train_ds = None
        self.val_ds = None
        self.test_ds = None

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

    def start_data_transformation(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()

        data_transformation = DataTransformation(config=data_transformation_config)
        self.train_ds, self.val_ds, self.test_ds = data_transformation.get_dataset()

    def start_model_training(self):
        model_trainer_config = self.config.get_model_trainer_config()

        model_trainer = ModelTrainer(config=model_trainer_config)

        model_trainer.train(
            train_ds=self.train_ds,
            val_ds=self.val_ds,
            test_ds=self.test_ds
        )
        
if __name__=="__main__":
    obj = TrainingPipeline()
    
    obj.start_data_ingestion()
    obj.start_data_validation()
    obj.start_data_transformation()
    obj.start_model_training()