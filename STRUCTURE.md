# Project Structure

This document describes the organization of the Customer Churn Prediction & Lifetime Value Engine project.

## Directory Layout

```
Customer-Churn-Prediction-Lifetime-Value-Engine/
│
├── 📓 notebooks/                          # Jupyter Notebooks (Analysis & Modeling)
│   ├── 01_data_exploration.ipynb          # EDA and data understanding
│   ├── 02_data_preprocessing.ipynb        # Data cleaning and preparation
│   ├── 03_model_training.ipynb            # Model development
│   ├── 04_model_comparison.ipynb          # Compare different models
│   ├── 05_feature_importance.ipynb        # Feature analysis
│   └── 06_customer_risk_scoring.ipynb     # Risk scoring and LTV
│
├── 📁 src/                                # Reusable Python Modules
│   ├── __init__.py                        # Package initialization
│   ├── data_loader.py                     # Data loading & validation
│   ├── preprocessing.py                   # Data preprocessing functions
│   ├── feature_engineering.py             # Feature creation & selection
│   ├── model_training.py                  # Model training utilities
│   └── evaluation.py                      # Model evaluation & visualization
│
├── 📁 data/                               # Data Storage
│   ├── raw/                               # Original, immutable data
│   │   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   └── processed/                         # Cleaned, processed data
│       └── customer_risk_scores.csv
│
├── 📁 models/                             # Trained Models & Artifacts
│   ├── churn_model.pkl                    # Saved churn prediction model
│   ├── ltv_model.pkl                      # Saved LTV model
│   └── model_performance.txt              # Performance metrics
│
├── 📁 dashboard/                          # Business Intelligence
│   └── Telco Customer Churn Analysis Dashboard.pbix
│
├── 📁 config/                             # Configuration Files
│   └── config.yaml                        # Project settings
│
├── 📁 logs/                               # Log Files
│   └── training.log                       # Training logs
│
├── 📄 README.md                           # Project overview
├── 📄 STRUCTURE.md                        # This file
├── 📄 requirements.txt                    # Python dependencies
├── 📄 .gitignore                          # Git ignore rules
└── 📄 Customer-Churn-Prediction-Lifetime-Value-Engine  # Project metadata
```

## File Descriptions

### Notebooks (`/notebooks`)
- **01_data_exploration.ipynb**: Initial data exploration, statistics, and visualizations
- **02_data_preprocessing.ipynb**: Data cleaning, missing value handling, and transformations
- **03_model_training.ipynb**: Model development and hyperparameter tuning
- **04_model_comparison.ipynb**: Compare multiple algorithms side-by-side
- **05_feature_importance.ipynb**: Analyze which features drive predictions
- **06_customer_risk_scoring.ipynb**: Generate customer risk scores and LTV predictions

### Source Modules (`/src`)
- **data_loader.py**: Functions for loading and validating data
- **preprocessing.py**: Data cleaning utilities (missing values, encoding, scaling)
- **feature_engineering.py**: Feature creation and selection functions
- **model_training.py**: Model training and persistence utilities
- **evaluation.py**: Evaluation metrics and visualization functions

### Data (`/data`)
- **raw/**: Original source data (read-only)
- **processed/**: Cleaned and transformed data ready for modeling

### Models (`/models`)
- Saved machine learning model files (`.pkl` format)
- Performance metrics and evaluation results

### Configuration (`/config`)
- **config.yaml**: Centralized configuration for data paths, model parameters, and settings

## How to Use

### 1. Setup Environment
```bash
pip install -r requirements.txt
```

### 2. Run Notebooks in Order
```bash
jupyter lab notebooks/
```

### 3. Import from src/ in Your Code
```python
from src.data_loader import load_data, validate_data
from src.preprocessing import handle_missing_values, scale_features
from src.model_training import train_random_forest, evaluate_model
```

### 4. Configure Settings
Edit `config/config.yaml` to modify:
- Data paths
- Model parameters
- Feature lists
- Training settings

## Best Practices

1. **Keep notebooks exploratory** - Use src/ modules for production code
2. **Never modify raw data** - Always work with copies
3. **Version your models** - Use timestamps or tags
4. **Document results** - Add findings to notebooks or README
5. **Test functions** - Write unit tests for src/ modules

## Next Steps

- [ ] Extract utility functions to `src/` modules
- [ ] Create unit tests in `tests/` directory
- [ ] Add data validation schemas
- [ ] Build API endpoint for model serving
- [ ] Create production deployment guide
