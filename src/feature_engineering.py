"""Module for feature engineering and selection"""

import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif
from typing import Tuple, List


def create_interaction_features(data: pd.DataFrame) -> pd.DataFrame:
    """
    Create interaction features from existing features.
    
    Args:
        data (pd.DataFrame): Input data
        
    Returns:
        pd.DataFrame: Data with interaction features
    """
    data_new = data.copy()
    
    # Example: Create interaction between tenure and monthly charges
    if 'tenure' in data.columns and 'MonthlyCharges' in data.columns:
        data_new['tenure_charge_interaction'] = data['tenure'] * data['MonthlyCharges']
    
    return data_new


def select_best_features(X: pd.DataFrame, y: pd.Series, k: int = 10) -> Tuple[List[str], pd.DataFrame]:
    """
    Select best features using SelectKBest.
    
    Args:
        X (pd.DataFrame): Features
        y (pd.Series): Target variable
        k (int): Number of best features to select
        
    Returns:
        Tuple[List[str], pd.DataFrame]: Selected feature names and data
    """
    selector = SelectKBest(score_func=f_classif, k=min(k, X.shape[1]))
    X_selected = selector.fit_transform(X, y)
    
    selected_features = X.columns[selector.get_support()].tolist()
    
    return selected_features, pd.DataFrame(X_selected, columns=selected_features)


def get_feature_importance(feature_names: List[str], importances: np.ndarray) -> pd.DataFrame:
    """
    Create DataFrame of feature importances.
    
    Args:
        feature_names (List[str]): Names of features
        importances (np.ndarray): Importance scores
        
    Returns:
        pd.DataFrame: Sorted feature importances
    """
    importance_df = pd.DataFrame({
        'feature': feature_names,
        'importance': importances
    }).sort_values('importance', ascending=False)
    
    return importance_df
