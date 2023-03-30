# Setup environment
conda create --name bikesharing\
conda activate bikesharing\
pip install requirements.txt 

# Run steamlit app
streamlit run dashboard.py

# Note
Before using it, you need to adjust bike_df = pd.read_csv('') in the bikesharing.py file according to the directory you have downloaded.
