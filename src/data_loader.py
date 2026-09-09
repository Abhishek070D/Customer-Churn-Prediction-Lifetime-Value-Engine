"""Module for loading and basic data validation"""

import pandas as pd
import numpy as np
from typing import Tuple


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load CSV data from file.
    
    Args:
        filepath (str): Path to CSV file
        
    Returns:
        pd.DataFrame: Loaded data
    """
    try:
        data = pd.read_csv(filepath)
        print(f"Data loaded successfully from {filepath}")
        print(f"Shape: {data.shape}")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None


def validate_data(data: pd.DataFrame) -> bool:
    """
    Validate data quality.
    
    Args:
        data (pd.DataFrame): Data to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if data is None:
        return False
    
    if data.empty:
        print("Error: Data is empty")
        return False
    
    missing_pct = (data.isnull().sum() / len(data) * 100)
    if missing_pct.max() > 50:
        print("Warning: Some columns have >50% missing values")
    
    return True


def get_data_info(data: pd.DataFrame) -> None:
    """
    Print data information.
    
    Args:
        data (pd.DataFrame): Data to analyze
    """
    print(f"\nData Shape: {data.shape}")
    print(f"\nData Types:\n{data.dtypes}")
    print(f"\nMissing Values:\n{data.isnull().sum()}")
