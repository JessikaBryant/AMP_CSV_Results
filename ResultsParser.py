############Parse Results from CSV and Results files to a Table and Figures for AMP predictions####
###import needed modules
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import sys

###read in files
amppredictorresults=pd.read_csv("InputFiles/DmollisAMPResults", sep="\t")
ampfeaturesresults=pd.read_csv("InputFiles/20240605_scored_features.csv", sep=",")
#print(len(ampfeaturesresults))
#print(len(amppredictorresults))

###add probability of AMP from amppredictedresults as a column to ampfeatures
#make empty column for new column
ampfeaturesresults.loc[:,"probability_AMP"]=""
#print(ampfeaturesresults.keys())
#add probability amp to ampfeatures
ampfeaturesresults["probability_AMP"]=amppredictorresults["probability_AMP"].to_numpy()
#print(ampfeaturesresults[0:5])

seqswithhighprobs=dict()

#find amp_probability >0.8
for probability in ampfeaturesresults["probability_AMP"]:
    if probability>=0.75:
        seqswithhighprobs[str(ampfeaturesresults["sequence_name"])]=""
        seqswithhighprobs[str(ampfeaturesresults["sequence_name"])]=probability
    print(seqswithhighprobs())
    break
sys.exit()

###Make scatter plot 
#x=x-axis = probability amp
#y=y-axis = hydrophobicity
#c=color
ax1=ampfeaturesresults.plot.scatter(x="probability_AMP",
                                    y="hydrophobicity.1.0",
                                    c='DarkBlue')
                                    
#save plot to pdf
ax1.savefig("scatterplothydrophobicity1.0", format="pdf")