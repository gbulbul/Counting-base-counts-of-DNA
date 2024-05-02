#counting DNA nucleotides
dna_nucleotides='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
def counting_nucleotides(dna_nucleotides): 
    count_A = 0
    count_G = 0 
    count_C = 0 
    count_T= 0
    for i in dna_nucleotides:
        if i == 'A':
           count_A = count_A + 1
        elif i == 'G' :
           count_G = count_G + 1
        elif i == 'C' :
           count_C = count_C + 1
        else :
           count_T= count_T+ 1
    # printing result
    return print("Count of A, G, C, T in dna_nucleotides are :", count_A, count_G, count_C, count_T)
counting_nucleotides(dna_nucleotides)    