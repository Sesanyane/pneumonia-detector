
# imports
import kaggle
import os
import shutil


# authentication
kaggle.api.authenticate()


# data retrieval
kaggle.api.dataset_download_files('paultimothymooney/chest-xray-pneumonia', unzip=True)
print("Completed data download.")


# data management
# data management
shutil.rmtree('chest_xray/__MACOSX')
shutil.rmtree('chest_xray/chest_xray')
os.rename('chest_xray', 'data')
print("Completed data management.")