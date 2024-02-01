from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd
import os

@data_loader
def load_data_from_file(*args, **kwargs):
    """
    Template for loading data from filesystem.
    Load data from 1 file or multiple file directories.

    For multiple directories, use the following:
        FileIO().load(file_directories=['dir_1', 'dir_2'])

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    folder_path = '/home/amal/projects/data-engineering-zoomcamp/data'
    file_list = os.listdir(folder_path)
    green_tripdata_files = [file for file in file_list if file.startswith("green_tripdata_")]

    for filename in green_tripdata_files:
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        print(df.head())

    return None


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
