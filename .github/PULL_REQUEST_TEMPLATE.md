## 📋 Pull Request: Repository Organization

### Title
**Organize repository structure with modular architecture and documentation**

### Description
This PR restructures the repository to improve maintainability, collaboration, and code reusability.

### Changes Made

#### ✅ New Directories & Files

1. **`src/` - Reusable Python Modules**
   - `data_loader.py` - Data loading and validation utilities
   - `preprocessing.py` - Data cleaning and transformation functions
   - `feature_engineering.py` - Feature creation and selection utilities
   - `model_training.py` - Model training and persistence functions
   - `evaluation.py` - Model evaluation and visualization tools
   - `__init__.py` - Package initialization

2. **`config/` - Configuration**
   - `config.yaml` - Centralized project configuration (data paths, model params, training settings)

3. **Documentation**
   - `requirements.txt` - Python dependencies (NumPy, Pandas, Scikit-learn, Jupyter, etc.)
   - `STRUCTURE.md` - Detailed project structure and file descriptions
   - `ORGANIZATION_GUIDE.md` - Usage guide and best practices
   - `.gitignore` - Git ignore rules for Python/data science projects

### Benefits

✨ **Code Reusability** - Extract functions from notebooks into reusable modules  \n🎯 **Clear Structure** - Organized directories for data, models, configs  \n📚 **Documentation** - Comprehensive guides for team members  \n🔧 **Configuration** - Centralized settings management via `config.yaml`  \n🚀 **Scalability** - Ready for production deployment and CI/CD pipelines  \n💾 **Data Safety** - Separation of raw (read-only) and processed data  \n\n### How to Use\n\n1. **Install dependencies**:\n   ```bash\n   pip install -r requirements.txt\n   ```\n\n2. **Import modules in notebooks**:\n   ```python\n   from src.data_loader import load_data\n   from src.preprocessing import handle_missing_values, scale_features\n   from src.model_training import train_random_forest, evaluate_model\n   ```\n\n3. **Configure settings**:\n   Edit `config/config.yaml` for data paths and model parameters\n\n### Existing Files (Unchanged)\n\n- ✅ `notebooks/` - All existing Jupyter notebooks remain unchanged\n- ✅ `data/raw/` - Original dataset (Telco Customer Churn)\n- ✅ `data/processed/` - Processed data files\n- ✅ `dashboard/` - Power BI dashboard\n- ✅ `README.md` - Project overview\n\n### Migration Path\n\nFor existing notebooks, gradually:\n1. Import functions from `src/` modules\n2. Replace cell code with module imports\n3. Focus notebooks on analysis and visualization\n\n### Testing\n\n- All existing notebooks will continue to work\n- No breaking changes to data or existing files\n- New modules follow scikit-learn conventions\n\n### File Statistics\n\n- **Files Added**: 11\n- **New Modules**: 5 Python files with 500+ lines of documented code\n- **Documentation**: 2 comprehensive guides\n- **Dependencies**: Centralized in `requirements.txt`\n\n### Related Issues\n\nN/A - Initial organization\n\n### Checklist\n\n- [x] Code follows project conventions\n- [x] Functions include docstrings\n- [x] Documentation is comprehensive\n- [x] No breaking changes to existing code\n- [x] Ready for team review\n\n---\n\n**Reviewer Notes**: Please check if the proposed structure aligns with team preferences. Adjustments can be made before merging.\n