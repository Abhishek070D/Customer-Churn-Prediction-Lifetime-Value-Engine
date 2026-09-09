"""Module for model evaluation and visualization utilities"""

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Any


def print_classification_report(y_true: np.ndarray, y_pred: np.ndarray) -> str:
    """
    Print detailed classification report.
    
    Args:
        y_true (np.ndarray): True labels
        y_pred (np.ndarray): Predicted labels
        
    Returns:
        str: Classification report
    """
    report = classification_report(y_true, y_pred)
    print(report)
    return report


def plot_confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray, title: str = "Confusion Matrix") -> None:
    """
    Plot confusion matrix.
    
    Args:
        y_true (np.ndarray): True labels
        y_pred (np.ndarray): Predicted labels
        title (str): Plot title
    """
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(title)
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.show()


def plot_feature_importance(importances: np.ndarray, feature_names: list, top_n: int = 15) -> None:
    """
    Plot feature importance.
    
    Args:
        importances (np.ndarray): Feature importance scores
        feature_names (list): Names of features
        top_n (int): Number of top features to display
    """
    indices = np.argsort(importances)[-top_n:]
    plt.figure(figsize=(10, 6))
    plt.barh(range(len(indices)), importances[indices])
    plt.yticks(range(len(indices)), [feature_names[i] for i in indices])
    plt.xlabel('Importance')
    plt.title('Feature Importance')
    plt.tight_layout()
    plt.show()


def calculate_metrics_summary(metrics: Dict[str, float]) -> pd.DataFrame:
    """
    Create DataFrame summary of metrics.
    
    Args:
        metrics (Dict[str, float]): Dictionary of metrics
        
    Returns:
        pd.DataFrame: Metrics summary
    """
    return pd.DataFrame(metrics, index=[0]).T
