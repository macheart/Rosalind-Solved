# Code to:
#1. Read a textfile 
#2. Clean the textfile
#3. Calculate the GC content of each DNA sequence within the file


f = open("rosalind_gc.txt",'r') # open the file on read mode
f = f.read() # read the whole text file and save as a string
chars="\n" # characters I want to eliminate in f
for char in chars: f=f.replace(char,"") # replace method
f # prints list f
f = f.split('>') # creates f into a list and splits at any character if unspecified in parentheses
f =f[1:] # remove empty string @ beginning of list (position 0)
f # file output 

seq_dict={} # initialize empty dictionary
info=[]
for string in f: # 
    seq=string[13:]
    ID=string[0:13]
    seq_dict[ID]=seq
    GC_count=0
    for nucl in seq:
        if nucl == 'G' or nucl =='C':
            GC_count +=1
            GC_content=100*(float(GC_count)/len(string)
#print ID, 100*(float(GC_count)/len(string)) # prints the seq info for the last sequence in the file!
    print ID, 100*(float(GC_count)/len(string)) # prints the seq info for all the strings!
