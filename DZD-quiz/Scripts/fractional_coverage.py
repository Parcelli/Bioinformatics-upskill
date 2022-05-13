#!/usr/bin/python3
#Reading the coverage tables with Pandas 
import pandas as pd
import sys
import csv

threshold=sys.argv[1]

df0=pd.read_table('sample0.txt', delim_whitespace=True,names=['chrom','start','end','depth'])
df1=pd.read_table('sample1.txt', delim_whitespace=True,names=['chrom','start','end','depth'])
df2=pd.read_table('sample2.txt', delim_whitespace=True,names=['chrom','start','end','depth'])
df3=pd.read_table('sample3.txt', delim_whitespace=True,names=['chrom','start','end','depth'])

#Define a function that calculates fractional coverage

def fractionalcoverage(df,threshold):
    "This function calculates fractional coverage"
    column='depth'
    count = (df[column] >= threshold).sum()
    # print (count)
    rows=len(df)
    fcov = count/rows
    return fcov
    
#Calling the function  
    
fcov0=fractionalcoverage(df0,threshold)
fcov1=fractionalcoverage(df1,threshold)
fcov2=fractionalcoverage(df2,threshold)
fcov3=fractionalcoverage(df3,threshold)

fcoverage={}
fcoverage={"sample0":fcov0 , "sample1":fcov1, "sample2":fcov2 , "sample3":fcov3}
print(fcoverage)
    
# converting the dictionary to a csv file
df=pd.DataFrame.from_dict(fcoverage, orient='index')
df.reset_index(inplace=True)
df.columns = ['sample','coverage']
df
#converting a dataframe to a csv
df.to_csv('coverage.csv',index=False)    
