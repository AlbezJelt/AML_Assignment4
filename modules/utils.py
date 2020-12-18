import numpy as np 
import os
import pandas as pd
import pickle

# Train dataset import function
def load_train_ds(dataset_path) :
    x_train = np.load(os.path.join(os.path.normpath(dataset_path), 'x_train.npz'))
    y_train = np.load(os.path.join(os.path.normpath(dataset_path), 'y_train.npz'))
    return x_train['arr_0'], y_train['arr_0']

# Test dataset import function
def load_test_ds(dataset_path) :
    x_test = np.load(os.path.join(os.path.normpath(dataset_path), 'x_test.npz'))
    y_test = np.load(os.path.join(os.path.normpath(dataset_path), 'y_test.npz'))
    return x_test['arr_0'], y_test['arr_0']

def custom_flatten(arr) :
    return arr.reshape(
        arr.shape[0],
        arr.shape[1] * arr.shape[2] * arr.shape[3])