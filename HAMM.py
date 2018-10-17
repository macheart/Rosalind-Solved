# Code to:
# 1. Open a file
# 2. Clean the file
# 3. Perform a sequence comparison and count base pairs that do not match

f=open('rosalind_hamm.txt','r') # open file on read mode
f=f.read() # set to read whole file
f=f.split() # remove newline characters
f1=f[0] # first sequence
f2=f[1] # second sequence
print 'sequence 1:', f1
print 'sequence 2:', f2

muts=0
for i in range(len(f1)): # perform an index based comparison of sequences
    if f2[i] != f1[i]: # if base @ specified index do not match 
        muts+=1 # count it, it's a mutation
print muts # print out total count
