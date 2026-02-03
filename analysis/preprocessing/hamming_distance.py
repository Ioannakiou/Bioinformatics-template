dna_str1 = "AGCTTAGCTA"
dna_str2 = "AGCTCGGCTA"


def h_d_loop(str1, str2):
    h_distance = 0
    for position in range(len(str1)):
        if str1[position] != str2[position]:
            h_distance += 1
    return h_distance

def h_d_set(str1, str2):
    nucleotide_set_1 = set([(x,y) for x, y in enumerate (str1)])
    nucleotide_set_2 = set([(x,y) for x, y in enumerate (str2)])

    # for x in range(len(nucleotide_set_1)):
    #     print(sorted(nucleotide_set_1)[x], sorted(nucleotide_set_2)[x])
        
    print(sorted(nucleotide_set_1.difference(nucleotide_set_2)))
        
    return len(nucleotide_set_1.difference(nucleotide_set_2))

def zip_h_d(str1, str2):
    # zipped_dna = zip(str1, str2)
    # for x in zipped_dna:
    #     print(x) # returns tuples of paired nucleotides
    
    return len([(n1, n2) for n1, n2 in zip(str1,str2) if n1 != n2])
    
    
        
print(f'Loop Hamming Distance between {dna_str1} and {dna_str2} is: ', end='')
print(h_d_loop(dna_str1, dna_str2))

print('Set Hamming Distance:')
print(h_d_set(dna_str1, dna_str2))

print('Zip Hamming Distance: ', end = '')
print(zip_h_d(dna_str1, dna_str2))