from src.chest_cancer.pipeline.training_pipeline import TrainingPipeline
if __name__ == "__main__":
    obj = TrainingPipeline()
    obj.start_data_ingestion()