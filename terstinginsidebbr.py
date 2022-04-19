# Databricks notebook source
!pip install mlflow

# COMMAND ----------

import os
import warnings
import sys

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet

import mlflow
import mlflow.sklearn


# COMMAND ----------

    # Read the wine-quality csv file (make sure you're running this from the root of MLflow!)
    data = pd.read_csv("wine-quality.csv")

# COMMAND ----------

data

# COMMAND ----------


