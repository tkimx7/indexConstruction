# -*- coding: utf-8 -*-
"""
Created on Wed May 28 15:06:49 2022

@author: ty
"""

import pandas as pd
import numpy as np

units = pd.read_csv("/home/ty/Desktop/Units.csv")
prices = pd.read_csv("/home/ty/Desktop/Prices.csv")

prices = prices.fillna(method='ffill')

del df
df = prices

df["a_units"] = units.iloc[0, 1]
df["b_units"] = units.iloc[1, 1]
df["c_units"] = units.iloc[2, 1]
df["d_units"] = units.iloc[3, 1]  

equity_notional = 7.3453215
basket_value = 1000
basket_unit = equity_notional/basket_value

for i in range(0, df.shape[0]):
    
    if (df.loc[i, "Date"] == "13-Jun-19"):
        
        df.loc[i, "a_units"] = units.iloc[0, 2]
        df.loc[i, "b_units"] = units.iloc[1, 2]
        df.loc[i, "c_units"] = units.iloc[2, 2]
        df.loc[i, "d_units"] = units.iloc[3, 2]
        
    if (df.loc[i, "Date"] == "18-Oct-19"):

        df.loc[i, "a_units"] = units.iloc[0, 3]
        df.loc[i, "b_units"] = units.iloc[1, 3]
        df.loc[i, "c_units"] = units.iloc[2, 3]
        df.loc[i, "d_units"] = units.iloc[3, 3]
        
df["basket_units"] = basket_unit
df["basket_value"] = 1000
df["a_units_asterisk"] = ""
df["b_units_asterisk"] = ""
df["c_units_asterisk"] = ""
df["d_units_asterisk"] = ""

for i in range(1, df.shape[0]):
    
    df.loc[i, "basket_value"] = (df.loc[i-1, "basket_value"] * 
                                (df.loc[i-1, "a_units"] * df.loc[i, "A"] + 
                                 df.loc[i-1, "b_units"] * df.loc[i, "B"] + 
                                 df.loc[i-1, "c_units"] * df.loc[i, "C"] + 
                                 df.loc[i-1, "d_units"] * df.loc[i, "D"]) / 
                                (df.loc[i-1, "a_units"] * df.loc[i-1, "A"] +  
                                 df.loc[i-1, "b_units"] * df.loc[i-1, "B"] + 
                                 df.loc[i-1, "c_units"] * df.loc[i-1, "C"] + 
                                 df.loc[i-1, "d_units"] * df.loc[i-1, "D"]))

    df.loc[i, "basket_units"] = (df.loc[i-1, "basket_units"] +  
                                ((df.loc[i, "a_units"] - df.loc[i-1, "a_units"]) * df.loc[i, "A"] +   
                                 (df.loc[i, "b_units"] - df.loc[i-1, "b_units"]) * df.loc[i, "B"] + 
                                 (df.loc[i, "c_units"] - df.loc[i-1, "c_units"]) * df.loc[i, "C"] + 
                                 (df.loc[i, "d_units"] - df.loc[i-1, "d_units"]) * df.loc[i, "D"]) / 
                                 df.loc[i, "basket_value"])
    
    df.loc[i, "a_units_asterisk"] = df.loc[i, "a_units"]/df.loc[i, "basket_units"]
    df.loc[i, "b_units_asterisk"] = df.loc[i, "b_units"]/df.loc[i, "basket_units"]
    df.loc[i, "c_units_asterisk"] = df.loc[i, "c_units"]/df.loc[i, "basket_units"]
    df.loc[i, "d_units_asterisk"] = df.loc[i, "d_units"]/df.loc[i, "basket_units"]
    

df_final = df[["Date", "basket_value","basket_units","a_units_asterisk","b_units_asterisk","c_units_asterisk","d_units_asterisk"]]

df_final.to_csv("/home/ty/Desktop/tykim_output.csv")














    
