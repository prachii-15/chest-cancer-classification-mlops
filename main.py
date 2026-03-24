from src.chest_cancer.pipeline.training_pipeline import TrainingPipeline

if __name__ == "__main__":
    obj = TrainingPipeline()
    
    try:
        print("🚀 Starting Pipeline...\n")

        # Step 1: Data Ingestion
        obj.start_data_ingestion()
        print("✅ Data Ingestion Done")

        # Step 2: Data Validation
        obj.start_data_validation()
        print("✅ Data Validation Done")

        # Step 3: Data Transformation (ADD THIS 🔥)
        obj.start_data_transformation()
        print("✅ Data Transformation Done")

        # Step 4: Model Training
        obj.start_model_training()
        print("✅ Model Training Done")

        print("\n🎉 Pipeline Completed Successfully!")

    except Exception as e:
        print("Error:", e)