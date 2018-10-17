# Code to:
# 1. Open file
# 2. Clean file
# 3. Count the frequencies of A, T, C, or G in a sequence

f=open('rosalind_dna.txt','r')
f=f.read() # file has a newline
chars="\n" # characters I want to eliminate in f
for char in chars: f=f.replace(char,"") # replace method

A_count=0
T_count=0
C_count=0
G_count=0
for char in f:
    if char == 'A':
        A_count+=1
    elif char == 'T':
        T_count+=1
    elif char == 'C':
        C_count+=1
    else:
        G_count+=1
print A_count, C_count, G_count, T_count
