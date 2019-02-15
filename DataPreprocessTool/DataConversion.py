import numpy as np
import pandas as pd
def drop_multi_col(col_names,df):
    '''
    AIM: drop cols by names
    :param col_names: col_names which are used to drop
    :param df: dataframe
    :return: updated df with dropped col
    '''
    df.drop(col_names,axis=1,inplace=True)
    return df

def change_dtypes(col_int,col_float,df):
    '''
     AIM : reduce memory by changing int64 to int32 and changing float64 to float32
    :param col_int: int64 cols
    :param col_float: float64 cols
    :param df: dataframe
    :return: update df with int32 and float32 cols
    '''
    df[col_int]=df[col_int].astype('int32')
    df[col_float]=df[col_float].astype('float32')
    return df
def check_missing_data(df):
    '''
    AIM:find NAN data in each cols and sort descending
    :param df:
    :return:
    '''
    return df.isnull().sum().sort_values(ascending=False)
def convert_cat2num(df):

    '''
    df.replace(toreplace,value)
    AIM: change category col with little values to num such as col_1 replace YES by 1 and NO by 0
    :param df:
    :return:
    '''
    num_encode = {'col_1': {'YES': 1, 'NO': 0},
                  'col_2': {'WON': 1, 'LOSE': 0, 'DRAW': 0}}
    df.replace(num_encode,inplace=True)
def concat_col_str_condition(df):
    '''
    concat 2 columns with strings if the last 3 letters of the first column are 'pil'
    :param df:
    :return:
    '''
    mask = df['col_1'].str.endswith('pil', na=False)
    col_new = df[mask]['col_1'] + df[mask]['col_2']
    col_new.replace('pil', ' ', regex=True, inplace=True)  # replace the 'pil' with emtpy space

def convert_str_datetime(df):
    '''
    AIM  :Convert datetime(String) to datetime(format we want)
    :param df:
    :return: updated df with new datetime format
    '''

    df.insert(loc=2, column='timestamp', value=pd.to_datetime(df.transdate, format='%Y-%m-%d %H:%M:%S.%f'))

def totalDescribe(df):
    '''
    AIM : describe df by unique value,Percentage of missing valuesv,,Percentage of values in the biggest category,data type for each col
    :param df:
    :return:
    '''
    stats=[]
    for col in df.columns:
        stats.append((col,df[col].nunique(),df[col].isnull().sum()*100/df.shape[0],df[col].value_counts(normalize=True, dropna=False).values[0] * 100,df[col].dtype))
    stats_df = pd.DataFrame(stats, columns=['Feature', 'Unique_values', 'Percentage of missing values',
                                            'Percentage of values in the biggest category', 'type'])
    stats_df.sort_values('Unique_values', ascending=False)
    return stats_df


if __name__=="__main__":
    drop_multi_col()
