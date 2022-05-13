#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
import csv
import sys

threshold=int(sys.argv[1])

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

# Initializing a dictionary and storing the output of the above function
fcoverage={}
fcoverage={"sample0":fcov0 , "sample1":fcov1, "sample2":fcov2 , "sample3":fcov3}
print(fcoverage)

#Coverting the dictionary to a dataframe

df=pd.DataFrame.from_dict(fcoverage, orient='index')
df.reset_index(inplace=True)
df.columns = ['sample','coverage']
df
#converting a dataframe to a csv
df.to_csv('coverage.csv',index=False)

#Plotting the frational coverage

y=df['coverage']
x=df['sample']

# Plot the data using bar() method
plt.bar(x, y, color='m')
plt.title("Genome fractional coverage")
plt.xlabel("Sample")
plt.ylabel("Fractional coverage")

# Show the plot
plt.show()
#plt.savefig('fcov.pdf')

