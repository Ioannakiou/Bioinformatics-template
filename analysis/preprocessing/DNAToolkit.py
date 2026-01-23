import collections  # noqa: F401

Nucleotides = ["A", "T", "C", "G"]

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
    # tmpFreq = {"A": 0, "T": 0, "C": 0, "G": 0}
    
    # for nuc in dna_seq:
    #     if nuc in tmpFreq:
    #         tmpFreq[nuc] += 1
    # return tmpFreq
    
    return dict(collections.Counter(dna_seq))
    
    