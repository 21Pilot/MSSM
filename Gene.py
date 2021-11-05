codondict = {}
fileIN = open("codons")
for line in fileIN:
    key, value = line.split()
    codondict[key] = value
    
print("* means it is the end of the gene")
print(codondict)


# Find the start and end, get only the middle part(location) of the sequence
    
# The [21562:25384] is taken from the output of the following info 
# Stated(shown) in the next cell 
    
from Bio.Seq import Seq
from Bio import SeqIO 
from Bio.SeqRecord import SeqRecord

for feature in seq_record.features:
    if feature.type == 'gene':
        gene = feature.qualifiers['gene'][0]
        start_pos = feature.location.start
        end_pos = feature.location.end
        print('Gene',gene,'location:',start_pos,'-',end_pos)
       
for seq_record in SeqIO.parse('NC_045512_sequence.gb','genbank'):
    print("The ID of the record is:",seq_record.id)
    print("The description of the target gene is:",seq_record.description)
    
    # SARS location
    seq_SARS = (str(seq_record.seq)[21562:25384])
    
# seq = seq_6 is the result of sequence processed in problem 4
seq = seq_6
# print("The original seq from problem 4 is", seq)

# Translate function using the codondict established from previous section 
def translate(s):
    table = codondict 
    protein = []
    end = len(s) - (len(s) %3) - 1
    for i in range(0,end,3):
        codon = s[i:i+3]
        if codon in table:
            aminoacid = table[codon]
            protein.append(aminoacid)
        else:
            protein.append("N")
    return "".join(protein)


# Output
print("The translated seq from problem 4 is ", translate(seq))
print("The translated SARS is", translate(seq_SARS))

# Save translated SARS to a txt file
# NOT necessary..
file = open("trans_seq_SARS.txt","w") 
file.write(translate(seq_SARS)) 
file.close() 

# Find GTNGTKR

trans_SARS = translate(seq_SARS)
search_seq = trans_SARS
  
# returns first occurrence of Substring
result = search_seq.find('GTNGTKR')
print ("Substring 'GTNGTKR' found at index",result, "of translated SARS sequence" )
