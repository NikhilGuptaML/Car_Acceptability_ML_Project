from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    # Ingest the data
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()

    # Transform the data
    data_transformation = DataTransformation()
    train_arr, test_arr,_= data_transformation.initiate_data_transformation(train_data_path, test_data_path)

    # Train the model
    model_trainer = ModelTrainer()
    model_trainer.initiate_model_trainer(train_arr, test_arr)
