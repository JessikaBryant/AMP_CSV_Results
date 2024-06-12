############Parse Results from CSV and Results files to a Table and Figures for AMP predictions####
###import needed modules
import pandas as pd
import numpy as np
#from matplotlib import pyplot as plt
from Bio import SeqIO 
import sys
import glob

"""###read in files
amppredictorresults=pd.read_csv("InputFiles/DmollisAMPResults", sep="\t")
#print(amppredictorresults.keys())

seqswithhighprobs=list()

#find amp_probability >0.8
#loop through every row in dataframe
for rownumber in amppredictorresults.index:
    tempProb=amppredictorresults.loc[rownumber]["probability_AMP"]
    tempSeqId=amppredictorresults.loc[rownumber]["seq_id"]
    if tempProb>=0.85:
        seqswithhighprobs.append(tempSeqId)

###Read in the clean fasta file and find the seqs with high probability

#Get the full path to the DNA sequence
seq_file_path = "/scratch/bryantj2/bb485/week09/CleanGenomes/DmollisOUT/GCA_032361265.1_ASM3236126v1_genomic_squeak.fa"

#open file
seq_file_handle = open(seq_file_path, "r")

#Create an empty dictionary
seq_dict = {}

#Loop through the lines in the file
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

#make an empty dictionary for high probability seqs to go
keepers_dict=dict()

#loop through dictionary of all of the seqs from clean fasta file
for k, v in seq_dict.items():
    if k in seqswithhighprobs: #ask if they are the same as the high probability seqs
        keepers_dict[k]=v #if that is true add to new dictionary


#calculate proportion of sequences kept (probabiilty >=0.8) from total sequences input
proportionkeepseqs=len(keepers_dict.keys())/len(seq_dict)
#print(proportionkeepseqs)

#write proportion to a text file to save 
proportionhandle=open("PredictedAMP_Proportion.txt", "a")
proportionhandle.write("The proportion of AMPs predicted by amPEPpy is " + str(proportionkeepseqs) +" for Dmollis")
proportionhandle.close()

###write clean high probability seqs to a new fasta file
#open file handle
handle=open("DmollisPredictedAMPs.fasta", "a")

#loop through keeper sequences
for k, v in keepers_dict.items():
    handle.write(">" + k +"\n") #write header line (sequence ID/name)
    handle.write(v + "\n") #write sequence line

#close fasta file
handle.close()
"""
#########Parse CSV Outputs From AxPEP Online##############
#read in all csv files
csvOutputFiles=glob.glob("/scratch/bryantj2/bb485/week09/AMP_CSV_Results/AxPEPResults/*Score.csv")

OutputSeqsWithHighprobs=list
#for loop to loop through each file, read it in, and work with it
for file in csvOutputFiles:
    tempfile=pd.read_csv(file, sep=",")
    #loop through every row in dataframe
    for rownumber in tempfile.index:
        tempprob=tempfile.loc[rownumber]["ampep"] #add prob of AMP to a temp list
        tempseqId=tempfile.loc[rownumber]["id"] #add accompanying seq name
        if tempprob>=0.85:
            OutputSeqsWithHighprobs.append("id")
            break
        
#print(OutputSeqsWithHighprobs())

###Make CSV File with Sequence, amPEPPy prob, AxPEP prob, length of predicted AMP seq
finaltable=pd.df()

