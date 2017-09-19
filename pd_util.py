#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 17:15:51 2017

@author: paulblankley
"""

# Some functions I have found to be useful in the past
import pandas as pd
import copy

def explode_value(df_in, col1, col2=None):
    """ This function is used when you have a list or two in your pandas 
    dataframe and you want to 'explode' (like the Hive feature out the 
    dataframe so your list now has a row for every element.
    ------------
    Example:        col1    col2    col3
                0   'mike'   [12,8]  ['dog','cat']
                1   'lucy'   [9,44]  ['mouse','lemon']
                ...
                explode_value(df, 'col2', 'col3')
    Example:        col1    col2    col3
                0   'mike'   12      'dog'
                1   'mike'   8       'cat'
                2   'lucy'   9       'mouse'   
                3   'lucy'   44      'lemon'
    -----------
    Args: df_in; Pandas Dataframe that contains the columns as lists that 
            you want to explode out.
          col1; string name of the column that you want to explode out.
          col2; string name of the second column that you want to explode 
            out.  (optional argument)
    -----------
    Returns: Pandas Dataframe that is exploded out by your chosen column(s)
    -----------
    Raises: ValueError in the case you do not input a dataframe or you have 
        columns with different lengths to blow out.
    """
    if not isinstance(df_in, pd.DataFrame):
        raise ValueError('You did not input a DataFrame.')
    new_obs = []
    if col2:
        # Case where col2 is passed
        for row in df_in.to_dict(orient='records'):
            breakout_col1= row[col1]
            breakout_col2 = row[col2]
            if len(breakout_col1)!= len(breakout_col2):
                raise ValueError('{0} and {1} are not the same length in row {2}'.format(col1,col2,row))
            del row[col1]
            del row[col2]
            for c1, c2 in zip(breakout_col1, breakout_col2):
                new_obs_row = copy.deepcopy(row)
                new_obs_row[col1] = c1
                new_obs_row[col2] = c2
                new_obs.append(new_obs_row)
        df_out = pd.DataFrame(new_obs)
        return df_out
    else:
        # Case where col2 is omitted
        for row in df_in.to_dict(orient='records'):
            breakout_col1= row[col1]
            if not isinstance(breakout_col1, list):
                print('Warning: The object | {0} | you are exploding out is not a list.'.format(breakout_col1))
            del row[col1]
            for c1 in breakout_col1:
                new_obs_row = copy.deepcopy(row)
                new_obs_row[col1] = c1
                new_obs.append(new_obs_row)
        df_out = pd.DataFrame(new_obs)
        return df_out

