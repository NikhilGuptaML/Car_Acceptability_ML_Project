import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from src.exception import CustomException
from src.logger import logging
from sklearn.impute import SimpleImputer
import os
from src.utils import save_object
from src.utils import evaluate,save_object

from sklearn.ensemble import RandomForestClassifier



@dataclass
class ModelTrainerConfig:
    trainedmodel_file_path=os.path.join('artifact',"model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Splitting test and train input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models={
                "Random Forest Classifier":RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
            }
            model_list=[]

            for i in range(len(models)):
                model=list(models.values())[i]
                model.fit(X_train,y_train)

                evaluate(model,X_train,y_train)
                evaluate(model,X_test,y_test)
                save_object(
                    file_path=self.model_trainer_config.trainedmodel_file_path,
                    obj=model
                )
        except Exception as e:
            raise CustomException(e,sys)