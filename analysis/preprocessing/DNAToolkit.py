from collections import Counter
from structures import Nucleotides, DNA_Reverse_Comp, DNA_Codons

def validateSeq(dna_seq):
    """Validate if a DNA sequence contains only valid nucleotides.

    Args:
        dna_seq (str): The DNA sequence to validate.
    """
    tmp_seq = dna_seq.upper()
    for nucleotide in tmp_seq:
        if nucleotide not in Nucleotides:
            return False 
    return tmp_seq 
    
def countNucFrequency(dna_seq):
    """Count the frequency of each nucleotide in a DNA sequence.

    Args:
        dna_seq (str): The DNA sequence to analyze.
    """
    tmpFreq = {"A": 0, "T": 0, "C": 0, "G": 0}
    
    for nuc in dna_seq:
        if nuc in tmpFreq:
            tmpFreq[nuc] += 1
    return  tmpFreq[nuc]
    
    # return dict(collections.Counter(dna_seq))
    
def transcribeDNAtoRNA(dna_seq):
    return dna_seq.replace("T", "U")

def reverseComplement(dna_seq):
    return ''.join(DNA_Reverse_Comp[nuc] for nuc in dna_seq[::-1])

def gc_content(dna_seq):
    """Calculate the GC content of a DNA sequence.

    Args:
        dna_seq (str): The DNA sequence to analyze.
    """
    gc_count = dna_seq.count("G") + dna_seq.count("C")
    return (gc_count / len(dna_seq)) * 100 

def gc_content_subseq(dna_seq, k=20):
    """Calculate the GC content of each subsequence of length k in a DNA sequence.

    Args:
        dna_seq (str): The DNA sequence to analyze.
        k (int): The length of each subsequence.
    """
    gc_contents = []
    for i in range(0, len(dna_seq) - k + 1, k):
        subseq = dna_seq[i:i + k]
        gc_contents.append(gc_content(subseq))
    return gc_contents
        
def translateDNAtoProtein(dna_seq, init_pos=0):
    """Translate a DNA sequence into a protein sequence.

    Args:
        dna_seq (str): The DNA sequence to translate.
    """
    return [DNA_Codons[dna_seq[pos:pos+3]] for pos in range(init_pos, len(dna_seq) -2, 3)] 

def codon_usage(dna_seq, aminoacid):
    """Calculate the codon frequency for each amino acid in a DNA sequence.

    Args:
        dna_seq (str): The DNA sequence to analyze.
    """
    tmpList = []
    for i in range(0, len(dna_seq) -2, 3):
        if DNA_Codons[dna_seq[i:i+3]] == aminoacid:
            tmpList.append(dna_seq[i:i+3])
            
    freqDict = dict(Counter(tmpList))
    totalWight = sum(freqDict.values()) 
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWight, 2)
    return freqDict