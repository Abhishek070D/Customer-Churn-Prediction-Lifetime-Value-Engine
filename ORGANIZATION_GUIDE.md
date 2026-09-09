# File Organization Guide

## Summary of Changes

This guide explains the reorganization of the Customer Churn Prediction & Lifetime Value Engine project for better maintainability and collaboration.

## What Was Added

### 1. **src/ - Reusable Python Modules**
   - **Purpose**: Centralize reusable code extracted from notebooks
   - **Files**:
     - `data_loader.py` - Load and validate data
     - `preprocessing.py` - Clean and prepare data
     - `feature_engineering.py` - Create and select features
     - `model_training.py` - Train and save models
     - `evaluation.py` - Evaluate and visualize results

### 2. **models/ - Model Artifacts**
   - **Purpose**: Store trained models and performance metrics
   - **Usage**: Save models with `src.model_training.save_model()`
   - **Format**: Pickle (`.pkl`) for scikit-learn models

### 3. **config/ - Configuration Files**
   - **config.yaml**: Centralized settings for:
     - Data paths
     - Model parameters
     - Feature lists
     - Training hyperparameters

### 4. **Documentation Files**
   - **requirements.txt**: Python package dependencies
   - **STRUCTURE.md**: Detailed project structure guide
   - **ORGANIZATION_GUIDE.md**: This file
   - **.gitignore**: Ignore unnecessary files in Git

## How to Use the New Structure

### In Jupyter Notebooks
```python
import sys
sys.path.insert(0, '..')
from src.data_loader import load_data
from src.preprocessing import handle_missing_values, scale_features
from src.model_training import train_random_forest, evaluate_model

# Load data
data = load_data('data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Preprocess
data_clean = handle_missing_values(data)

# Train model
X_train, X_test, y_train, y_test = train_test_split_data(X, y)
model = train_random_forest(X_train, y_train)
metrics = evaluate_model(model, X_test, y_test)
```

### From Command Line
```bash
# Install dependencies
pip install -r requirements.txt

# Run notebooks
jupyter notebook notebooks/

# Use Python scripts
python -c "from src.data_loader import load_data; print(load_data('data/raw/...'))"
```

## Migration Guide

If you have existing code in notebooks:

1. **Identify reusable functions** in your notebooks
2. **Copy them** to appropriate `src/` module
3. **Test the functions** independently
4. **Update notebook imports** to use the modules
5. **Keep notebook cell count minimal** - focus on analysis, not implementation

## File Naming Conventions

- **Notebooks**: `NN_description.ipynb` (e.g., `01_data_exploration.ipynb`)
- **Python modules**: `snake_case.py` (e.g., `data_loader.py`)
- **Data files**: `descriptive_name.csv` (e.g., `customer_risk_scores.csv`)
- **Models**: `model_type_date.pkl` (e.g., `churn_model_20240901.pkl`)

## Directory Permissions

- **data/raw**: Read-only (never modify original data)
- **data/processed**: Read-write (intermediate results)
- **models**: Read-write (save trained models)
- **notebooks**: Read-write (analysis and experiments)
- **src**: Read-write (update shared functions)

## Best Practices Going Forward

### ✅ DO
- Keep notebooks focused on analysis and visualization
- Extract utility functions to `src/`
- Use `config.yaml` for parameterization
- Save models in `models/` directory
- Document your functions with docstrings
- Version your models with timestamps

### ❌ DON'T
- Modify raw data files directly
- Hard-code paths or parameters
- Mix preprocessing logic with analysis
- Store large files in the repository
- Commit model files to Git (use `.gitignore`)

## Troubleshooting

**Import errors in notebooks?**
```python
import sys
sys.path.insert(0, '..')
from src.data_loader import load_data
```

**Missing dependencies?**
```bash
pip install -r requirements.txt --upgrade
```

**Data file not found?**
- Ensure you're running from repo root
- Check paths in `config/config.yaml`
- Use absolute paths when needed

## Questions?

Refer to `STRUCTURE.md` for detailed documentation or review the docstrings in `src/` modules.
