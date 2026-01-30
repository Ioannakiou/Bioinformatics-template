from bio_structs import DNA_Nucleotides
import random

class bio_seq:
    """DNA sequence class. Default value: ATCG, DNA, No label"""

    def __init__(self, seq="ATCG", seq_type="DNA", label="No label"):
        """Initialize a DNA sequence object."""
        self.seq = seq.upper()
        self.label = label
        self.seq_type = seq_type
        self.is_valid = self.__validateSeq()
        assert self.is_valid, f"Invalid DNA sequence: {self.seq}"

    # DNA Toolkit functions as methods:
    def __validateSeq(self):
        """Validate if a DNA sequence contains only valid nucleotides.

        Args:
            dna_seq (str): The DNA sequence to validate.
        """
        return set(DNA_Nucleotides).issuperset(self.seq)
    
    def get_seq_biotype(self):
        return self.seq_type
    
    def get_seq_info(self):
        """Display sequence information."""
        return f"Label: {self.label} | Type: {self.seq_type} | Sequence: {self.seq} | Length: {len(self.seq)}"
    
    def generate_random_seq(self, length=50, seq_type="DNA"):
        """Generate a random DNA sequence of given length."""
        seq = ''.join([random.choice(DNA_Nucleotides) for _ in range(length)])
        self.__init__(seq, seq_type, "Randomly Generated Sequence")
    
    
        