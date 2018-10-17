# Code to:
# 1. Open file
# 2. Clean file
# 3. Transcribe a given DNA sequence 

f=open('rosalind_rna.txt','r')
f=f.read() # file has a newline

chars="\n" # characters I want to eliminate in f
for char in chars: f=f.replace(char,"") # replace method

f=f.replace('T','U')
f
