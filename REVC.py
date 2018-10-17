# Code to:
# 1. Open a text file 
# 2. Clean the text file
# 3. Reverse the DNA sequence and 

f=open('rosalind_revc.txt','r')
f=f.read() # necessary
f=f.replace('\n','')
print 'sequence:', f


f_rev=f[::-1] # reverse the sequence, you can also apply reverse()
print 'reverse sequence:', f_rev

f_rev_c = '' # initializde a new string
# NOTE: using replace() on f_rev creates problems
for nucl in f_rev:
    if nucl == 'A':
        f_rev_c += 'T' #  appending to new string the reverse complement of f
    elif nucl == 'T':
        f_rev_c+='A'
    elif nucl == 'G':
        f_rev_c += 'C'
    else:
        f_rev_c +='G'
print 'reverse complement:', f_rev_c
