"""Module for data preprocessing and cleaning"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from typing import Tuple, List


def handle_missing_values(data: pd.DataFrame, strategy: str = 'drop') -> pd.DataFrame:
    """
    Handle missing values in dataset.
    
    Args:
        data (pd.DataFrame): Input data
        strategy (str): 'drop' or 'mean' or 'median'
        
    Returns:
        pd.DataFrame: Cleaned data
    """
    if strategy == 'drop':
        return data.dropna()
    elif strategy == 'mean':
        return data.fillna(data.mean(numeric_only=True))
    elif strategy == 'median':
        return data.fillna(data.median(numeric_only=True))
    return data


def remove_duplicates(data: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows.
    
    Args:
        data (pd.DataFrame): Input data
        
    Returns:
        pd.DataFrame: Data without duplicates
    """
    initial_rows = len(data)
    data = data.drop_duplicates()
    print(f"Removed {initial_rows - len(data)} duplicate rows")
    return data


def encode_categorical(data: pd.DataFrame, categorical_cols: List[str]) -> pd.DataFrame:
    """
    Encode categorical variables.
    
    Args:
        data (pd.DataFrame): Input data
        categorical_cols (List[str]): List of categorical column names
        
    Returns:
        pd.DataFrame: Data with encoded categorical variables
    """
    data_encoded = data.copy()
    
    for col in categorical_cols:
        if col in data_encoded.columns:
            le = LabelEncoder()
            data_encoded[col] = le.fit_transform(data_encoded[col].astype(str))
    
    return data_encoded


def scale_features(X: pd.DataFrame, numerical_cols: List[str]) -> Tuple[pd.DataFrame, StandardScaler]:
    """
    Scale numerical features.
    
    Args:
        X (pd.DataFrame): Input features
        numerical_cols (List[str]): List of numerical column names
        
    Returns:
        Tuple[pd.DataFrame, StandardScaler]: Scaled features and scaler object
    """
    scaler = StandardScaler()
    X_scaled = X.copy()
    
    if numerical_cols:
        X_scaled[numerical_cols] = scaler.fit_transform(X[numerical_cols])
    
    return X_scaled, scaler
