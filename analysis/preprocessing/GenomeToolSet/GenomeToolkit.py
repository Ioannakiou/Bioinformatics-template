class genomeToolkit:
    def __init__(self):
        print("Genome Toolkit initialized.")


    def count_kmer(self, sequence, kmer):
        # sourcery skip: inline-immediately-returned-variable, sum-comprehension
        """Counts repeating k-mers in a given sequence. Includes overlapping k-mers."""
        kmer_count = 0
        for position in range(len(sequence) - len(kmer) -1):
            print(sequence[position:position + len(kmer)], "=", kmer)
            if sequence[position:position + len(kmer)] == kmer:
                kmer_count += 1
        return kmer_count
    
    
"""
seq = AATGCGAAAC | Legnth: 10
kmer AA            | Length: 2
Loops: len(sequence) - (len(kmer) -1)
Loops
"""