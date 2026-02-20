########################
###SETUP & DATA LOAD
########################

## install packages if needed
#pip install pandas numpy datetime

## import packages, run every time 
import pandas as pd, numpy as np, datetime 


### Load data snapshots
df1 = pd.read_csv("snapshot_1.csv")
df2 = pd.read_csv("snapshot_2.csv")


## Put data frames into a list for easier handling and to make code flexible
dflist = [df1, df2] 


########################
### TEST
########################

## Check if headers match, show mismatches
print(set(df1.columns) - set(df2.columns), set(df2.columns) - set(df1.columns))

##Confirm headers match exactly
print(df1.columns.equals(df2.columns))

#count missing values for all columns
for df in dflist:
    print(df.isna().sum())
    
#count duplicated records
for df in dflist:
    print(df.duplicated().sum())
    
#confirm changes were successful
for df in dflist:
    print(df.info())

#confirm changes were successful
for df in dflist:
    print(df.info())
    

