#!/usr/bin/python3
#Reading the coverage tables with Pandas 
import pandas as pd

df0=pd.read_table('sample0.txt', delim_whitespace=True,names=['chrom','start','end','depth'])
df1=pd.read_table('sample1.txt', delim_whitespace=True,names=['chrom','start','end','depth'])
df2=pd.read_table('sample2.txt', delim_whitespace=True,names=['chrom','start','end','depth'])
df3=pd.read_table('sample3.txt', delim_whitespace=True,names=['chrom','start','end','depth'])


#Define a function that calculates fractional coverage

def fractionalcoverage(df,threshold):
    "This function calculates fractional coverage"
    column='depth'
    count = (df[column] >= threshold).sum()
    rows=len(df)
    fcov = count/rows
    print(fcov)
    
#HELP: Reading this output to a csv file  
    
fcov0=fractionalcoverage(df0,5)
fcov0
fcov1=fractionalcoverage(df1,5)
fcov2=fractionalcoverage(df2,5)
fcov3=fractionalcoverage(df3,5)

fcoverage={}
fcoverage={"sample0":fcov0 , "sample1":fcov1, "sample2":fcov2 , "sample3":fcov3}
print(fcoverage)
#Reading the output of the fractionalcoverage function to a csv file

import csv

with open('fractional_coverage.csv', 'w', newline='') as csvfile:
    fieldnames = ['sample_name', 'fractionalcoverage']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'sample_name': 'sample0', 'fractionalcoverage': 0.6307692307692307})
    writer.writerow({'sample_name': 'sample1', 'fractionalcoverage': 1.0})
    writer.writerow({'sample_name': 'sample2', 'fractionalcoverage': 0.23376623376623376})
    writer.writerow({'sample_name': 'sample3', 'fractionalcoverage': 0.9734848484848485})
    
