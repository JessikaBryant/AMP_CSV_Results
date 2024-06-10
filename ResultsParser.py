############Parse Results from CSV and Results files to a Table and Figures for AMP predictions####
###import needed modules
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from Bio import SeqIO 
import sys

###read in files
amppredictorresults=pd.read_csv("InputFiles/DmollisAMPResults", sep="\t")
#ampfeaturesresults=pd.read_csv("InputFiles/20240605_scored_features.csv", sep=",")
#print(len(ampfeaturesresults))
#print(amppredictorresults.keys())
#sys.exit()

###add probability of AMP from amppredictedresults as a column to ampfeatures
#make empty column for new column
#ampfeaturesresults.loc[:,"probability_AMP"]=""
#print(ampfeaturesresults.keys())
#add probability amp to ampfeatures
#ampfeaturesresults["probability_AMP"]=amppredictorresults["probability_AMP"].to_numpy()
#print(ampfeaturesresults[0:5])

seqswithhighprobs=list()
counter=0


#find amp_probability >0.8
#loop through every row in dataframe
for rownumber in amppredictorresults.index:
    tempProb=amppredictorresults.loc[rownumber]["probability_AMP"]
    tempSeqId=amppredictorresults.loc[rownumber]["seq_id"]
    if tempProb>=0.85:
        seqswithhighprobs.append(tempSeqId)
    
    counter+=1
    if counter>100000:
        break

###Read in the clean fasta file and find the seqs with high probability
# Read in the DNA sequence associated with the annotations

#Get the full path to the DNA sequence
seq_file_path = "/scratch/bryantj2/bb485/week09/CleanGenomes/DmollisOUT/GCA_032361265.1_ASM3236126v1_genomic_squeak.fa"

seq_file_handle = open(seq_file_path, "r")

#Create an empty dictionary
seq_dict = {}

#Loop through the line in the file
for line in seq_file_handle:
    if line.startswith(">"):
        id_temp = line.strip() #Removes "\n"
        id_clean = id_temp.replace(">", "") #Removes ">" by replacing with nothing.
        
        #Add the item to the dictionary
        seq_dict[id_clean]="" # id_clean is the key, the value is an empty string (for now)
    else:
        seq_line = line.strip() #Removes "\n"
        
        #append this line to the dictionary value, using the key (which is still "id_clean" from the previous line)
        seq_dict[id_clean] += seq_line


keepers_dict=dict()

for k, v in seq_dict.items():
    if k in seqswithhighprobs:
        keepers_dict[k]=v


#proportion of sequences kept (probabiilty >=0.8) from total sequences input
proportionkeepseqs=len(keepers_dict.keys())/len(seq_dict)
#print(proportionkeepseqs)

proportionhandle=open("PredictedAMP_Proportion.txt", "a")
proportionhandle.write("The proportion of AMPs predicted by amPEPpy is " + str(proportionkeepseqs) +" for Dmollis")
proportionhandle.close()


handle=open("DmollisPredictedAMPs.fasta", "a")

for k, v in keepers_dict.items():
    handle.write(">" + k +"\n") 
    handle.write(v + "\n")

handle.close()

sys.exit()


"""
with open("Test1.fasta", "w") as handle:
    SeqIO.write(kee.values(), handle, 'fasta')

sys.exit()"""

#loop through the amp_probability for seqs greater than 0.7 and add seq names either to a list or a dict w/ probability



"""for seqname in amppredictorresults["seq_id"]:
    tempseqdict=dict()
    tempseqdict[str(seqname)]=""    
    for probability in amppredictorresults["probability_AMP"]:
        tempseqdict[seqname]=probability
        #print(tempseqdict)
        if probability>=0.7:
            seqswithhighprobs=tempseqdict[seqname]
            print(seqswithhighprobs)
            break
        sys.exit()"""
            
        




###Make scatter plot 
#x=x-axis = probability amp
#y=y-axis = hydrophobicity
#c=color
ax1=ampfeaturesresults.plot.scatter(x="probability_AMP",
                                    y="hydrophobicity.1.0",
                                    c='DarkBlue')
                                    
#save plot to pdf
ax1.savefig("scatterplothydrophobicity1.0", format="pdf")