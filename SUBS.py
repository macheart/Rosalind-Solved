# Code to:
# 1. Open a text file
# 2. Clean the file
# 3. Find the positions of a motif within a sequence (note, not python index)

import re # import to perform motif search

f=open('rosalind_subs.txt','r') # open file on read mode
f=f.read() # set to read whole file
f=f.split()
seq=f[0]
motif=f[1]
print 'sequence:',seq
print 'motif:', motif

motif_count=0 # initialize to search at the beginning (python idex)
while motif_count != -1 : # so long as it's in the sequence, -1 means not found
        motif_count = seq.find(motif,motif_count+1) # find() starts search at indicated position, REPORTS BOOLEAN
        print motif_count+1
        
