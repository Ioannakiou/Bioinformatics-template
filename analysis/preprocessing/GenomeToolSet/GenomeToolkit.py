class genomeToolkit:
    def __init__(self):
        print("Genome Toolkit initialized.")


    def count_kmer(self, sequence, kmer):
        # sourcery skip: inline-immediately-returned-variable, sum-comprehension
        """
        Counts the number of times a specific k-mer appears in a given sequence, 
        including overlapping k-mers.
        
        Parameters:
            sequence (str): The DNA sequence to search in.
            kmer (str): The specific k-mer to search for in the sequence.
            
        Returns: 
            int: The number of times the k-mer appears in the sequence.
        """
        kmer_count = 0
        for position in range(len(sequence) - len(kmer) -1):
            print(sequence[position:position + len(kmer)], "=", kmer)
            if sequence[position:position + len(kmer)] == kmer:
                kmer_count += 1
        return kmer_count
    
    def find_most_frequent_kmers(self, sequence, k_len):
        """
        Finds the most frequent k-mers of a given length in a DNAstring
        
        Parameters:
            sequence (str): The DNA string to search.
            k_len (int): The length of the k-mers to search for.
            
        Returns:
            list: A list of the most frequent k-mers in the DNA string.
        """
        # Initialize a dictionary to store k-mer frequencies
        kmer_frequencies = {}
        
        # Loop through the DNA string and count k-mer frequencies
        for position in range(len(sequence) - k_len + 1):
            kmer = sequence[position:position + k_len]
            if kmer in kmer_frequencies:
                kmer_frequencies[kmer] += 1
            else:
                kmer_frequencies[kmer] = 1    
        # Find the highest frequency of any k-mer
        highest_frequency = max(kmer_frequencies.values())
        
        return [kmer for kmer, frequency in kmer_frequencies.items() if frequency == highest_frequency]

    
"""
seq = AATGCGAAAC | Legnth: 10
kmer AA            | Length: 2
Loops: len(sequence) - (len(kmer) -1)
Loops
"""