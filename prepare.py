
def remove_outliers(df, k, col_list):
    ''' remove outliers from a list of columns in a dataframe 
        and return that dataframe
    '''
    
    for col in col_list:
        # get quartiles
        q1, q3 = df[f'{col}'].quantile([.25, .75])  
        # calculate interquartile range
        iqr = q3 - q1   
        # get upper bound
        upper_bound = q3 + k * iqr 
        # get lower bound
        lower_bound = q1 - k * iqr   

        # return dataframe without outliers
        
        df = df[(df[f'{col}'] > lower_bound) & (df[f'{col}'] < upper_bound)]
        
    return df