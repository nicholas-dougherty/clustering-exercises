#                         _       ______  ___    _   __________    ______                           #           
#                        | |     / / __ \/   |  / | / / ____/ /   / ____/                           #           
#                        | | /| / / /_/ / /| | /  |/ / / __/ /   / __/                              #           
#                        | |/ |/ / _, _/ ___ |/ /|  / /_/ / /___/ /___                              #           
#                        |__/|__/_/ |_/_/  |_/_/ |_/\____/_____/_____/                              #             
#--------------------------------------------------------------------------------------------------|#
#--------------------------------------------------------------------------------------------------|#
# imports
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler
import scipy.stats as stats
from env import get_db_url
from sklearn.model_selection import train_test_split
#--------------------------------------------------------------------------------------------------|#
#--------------------------------------------------------------------------------------------------|#
def wrangle_mall():
    train, validate, test = prepare_mall(get_mallcustomer_data())
    
    return train, validate, test
#--------------------------------------------------------------------------------------------------|#
def get_mallcustomer_data():
    df = pd.read_sql('SELECT * FROM customers;', get_db_url('mall_customers'))
    return df.set_index('customer_id')
#--------------------------------------------------------------------------------------------------|#
def split_data(df, seed=123):
    '''
    This function takes in a pandas dataframe and a random seed. It splits the original
    data into train, test and split dataframes and returns them.
    Test dataset is 20% of the original dataset
    Train is 56% (0.7 * 0.8 = .56) of the original dataset
    Validate is 24% (0.3 * 0.7 = 0.24) of the original dataset
    '''
    train, test = train_test_split(df, train_size=0.8, random_state=seed)
    train, validate = train_test_split(train, train_size=0.7, random_state=seed)
    
    print('Train: %d rows, %d cols' % train.shape)
    print('Validate: %d rows, %d cols' % validate.shape)
    print('Test: %d rows, %d cols' % test.shape)
    return train, validate, test
#--------------------------------------------------------------------------------------------------|#
def one_hot_encode(df):
    '''
    This function takes in a dataframe and one hot encodes
    the gender column and drops the original column before returning the dataframe.
    '''
    df['is_female'] = df.gender == 'Female'
    df = df.drop(columns='gender')
    
    return df

def prepare_mall(df):
    df = one_hot_encode(df)
    train, validate, test = split_data(df)
    
    return train, validate, test
#--------------------------------------------------------------------------------------------------|#
def scale_data(train, validate, test):
    '''
    This function takes in the features for train, validate and test splits.
    It creates a MinMax Scaler and fits that to the train set.
    It then transforms the validate and test splits and returns the scaled features
    for the train, validate and test splits.
    '''
    columns_to_scale = ['age', 'spending_score', 'annual_income']
    train_scaled = train.copy()
    validate_scaled = validate.copy()
    test_scaled = test.copy()

    scaler = MinMaxScaler()
    scaler.fit(train[columns_to_scale])

    train_scaled[columns_to_scale] = scaler.transform(train[columns_to_scale])
    validate_scaled[columns_to_scale] = scaler.transform(validate[columns_to_scale])
    test_scaled[columns_to_scale] = scaler.transform(test[columns_to_scale])

    return train_scaled, validate_scaled, test_scaled
#--------------------------------------------------------------------------------------------------|#
def get_exploration_data():
    df = get_mallcustomer_data()
    train, validate, test = split(df)
    return train
#--------------------------------------------------------------------------------------------------|#
def get_modeling_data(scale_data=False):
    df = get_mallcustomer_data()
    df = one_hot_encode(df)
    train, validate, test = split(df)
    if scale_data:
        return scale(train, validate, test)
    else:
        return train, validate, test
#--------------------------------------------------------------------------------------------------|#
#--------------------------------------------------------------------------------------------------|#
#--------------------------------------------------------------------------------------------------|#