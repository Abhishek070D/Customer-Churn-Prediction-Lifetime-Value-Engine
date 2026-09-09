"""Module for model training and evaluation"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import joblib
from typing import Tuple, Dict, Any


def train_test_split_data(X: pd.DataFrame, y: pd.Series, test_size: float = 0.2, 
                          random_state: int = 42) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Split data into training and testing sets.
    
    Args:
        X (pd.DataFrame): Features
        y (pd.Series): Target variable
        test_size (float): Proportion of test data
        random_state (int): Random seed
        
    Returns:
        Tuple: X_train, X_test, y_train, y_test
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def train_random_forest(X_train: pd.DataFrame, y_train: pd.Series, n_estimators: int = 100) -> RandomForestClassifier:
    """
    Train Random Forest model.
    
    Args:
        X_train (pd.DataFrame): Training features
        y_train (pd.Series): Training target
        n_estimators (int): Number of trees
        
    Returns:
        RandomForestClassifier: Trained model
    """
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model: Any, X_test: pd.DataFrame, y_test: pd.Series) -> Dict[str, float]:
    """
    Evaluate model performance.
    
    Args:
        model: Trained model
        X_test (pd.DataFrame): Test features
        y_test (pd.Series): Test target
        
    Returns:
        Dict: Evaluation metrics
    """
    y_pred = model.predict(X_test)
    
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, average='weighted'),
        'recall': recall_score(y_test, y_pred, average='weighted'),
        'f1': f1_score(y_test, y_pred, average='weighted')
    }
    
    return metrics


def save_model(model: Any, filepath: str) -> None:
    """
    Save trained model to file.
    
    Args:
        model: Trained model
        filepath (str): Path to save model
    """
    joblib.dump(model, filepath)
    print(f"Model saved to {filepath}")


def load_model(filepath: str) -> Any:
    """
    Load trained model from file.
    
    Args:
        filepath (str): Path to model file
        
    Returns:
        Trained model
    """
    model = joblib.load(filepath)
    print(f"Model loaded from {filepath}")
    return model
