from bio_structs import NUCLEOTIDE_BASE, DNA_Codons, RNA_Codons
from collections import Counter
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
        """Validate if a DNA sequence contains only valid nucleotides."""
        return set(NUCLEOTIDE_BASE[self.seq_type]).issuperset(self.seq)
    
    def countNucFrequency(self):
        """Count the frequency of each nucleotide in a DNA sequence."""
        return {nuc: self.seq.count(nuc) for nuc in NUCLEOTIDE_BASE[self.seq_type]}
    
    def transcribeDNAtoRNA(self):
        """Transcribe DNA sequence to RNA sequence."""
        if self.seq_type == "DNA":
            return self.seq.replace("T", "U")
        return "Not a DNA sequence"
            
    def reverseComplement(self):
        """Get the reverse complement of the DNA sequence."""
        if self.seq_type == "DNA":
            mapping = str.maketrans('ATCG', 'TAGC')
        else:
            mapping = str.maketrans('AUCG', 'UAGC')
        return self.seq.translate(mapping)[::-1]
    
    def gc_content(self):
        """Calculate the GC content of the DNA sequence."""
        return round((self.seq.count("G") + self.seq.count("C")) / len(self.seq) * 100)
    
    def translateDNAtoProtein(self, init_pos=0):
        """Translate a DNA sequence into a protein sequence."""
        if self.seq_type == "DNA":
            return [DNA_Codons[self.seq[pos:pos+3]] for pos in range(init_pos, len(self.seq)-2, 3)]
        elif self.seq_type == "RNA":
            return [RNA_Codons[self.seq[pos:pos+3]] for pos in range(init_pos, len(self.seq)-2, 3)]        
        
    def get_seq_biotype(self):
        return self.seq_type
    
    def get_seq_info(self):
        """Display sequence information."""
        return f" [Label]: {self.label} \n [Type]: {self.seq_type} \n [Sequence]: {self.seq} \n [Length]: {len(self.seq)}"
    
    def generate_random_seq(self, length=50, seq_type="DNA"):
        """Generate a random DNA sequence of given length."""
        seq = ''.join([random.choice(NUCLEOTIDE_BASE[seq_type]) for _ in range(length)])
        self.__init__(seq, seq_type, "Randomly Generated Sequence")
    
    def gc_content_subseq(self, k=20):
        """Calculate the GC content of each subsequence of length k in a DNA sequence."""
        res = []
        for i in range(0, len(self.seq) - k + 1, k):
            subseq = self.seq[i:i + k]
            gc_count = round((subseq.count("G") + subseq.count("C")) / len(subseq) * 100)
            res.append(gc_count)
        return res
    
    def codon_usage(self, amino_acid):
        """Provides the codon frequency for a given amino acid in the DNA sequence."""
        tmpList = []
        if self.seq_type == "DNA":
            for i in range(0, len(self.seq) -2, 3):
                if DNA_Codons[self.seq[i:i+3]] == amino_acid:
                    tmpList.append(self.seq[i:i+3])
        elif self.seq_type == "RNA":
            for i in range(0, len(self.seq) -2, 3):    
                if RNA_Codons[self.seq[i:i+3]] == amino_acid:
                    tmpList.append(self.seq[i:i+3])
        freqDict = dict(Counter(tmpList))
        totalWight = sum(freqDict.values()) 
        for seq in freqDict:
            freqDict[seq] = round(freqDict[seq] / totalWight, 2)
        return freqDict
        
    def gen_reading_frames(self):  # sourcery skip: merge-list-append, merge-list-appends-into-extend, merge-list-extend, unwrap-iterable-construction
        frames = []
        frames.append(self.translateDNAtoProtein(0))
        frames.append(self.translateDNAtoProtein(1))
        frames.append(self.translateDNAtoProtein(2))
        tmp_seq = bio_seq(self.reverseComplement(), self.seq_type)
        frames.append(tmp_seq.translateDNAtoProtein(0))
        frames.append(tmp_seq.translateDNAtoProtein(1))
        frames.append(tmp_seq.translateDNAtoProtein(2))
        del tmp_seq
        return frames
    
    def proteins_from_rf(self, aa_seq):    # sourcery skip: for-index-underscore
        """Compute all possible proteins from a reading frame amino acid sequence and return a list of proteins."""
        current_protein = []
        proteins = []
        for aa in aa_seq:
            if aa == '_': # Stop codon
                if current_protein:
                    for p in current_protein:
                        proteins.append(p)
                    current_protein = []
            else:
                if aa == 'M': # Start codon
                    current_protein.append("")
                for i in range(len(current_protein)):
                    current_protein[i] += aa
        return proteins
    
    def all_proteins_from_orfs(self, startReadPos=0, endReadPos=0, ordered=False):
    # sourcery skip: assign-if-exp, for-append-to-extend, reintroduce-else, simplify-generator
        """ Compute all possible proteins from all open reading frames"""
        """Protein search DB: https://www.ncbi.nlm.nih.gov/nuccore/NM_001185097.2/"""
        """ API can be used to fetch protein info"""
        if endReadPos > startReadPos:
            tmpseq = bio_seq(self.seq[startReadPos:endReadPos], self.seq_type)
            rfs = tmpseq.gen_reading_frames()
        else:
            rfs = self.gen_reading_frames()
            
        res = []
        for rf in rfs:
            proteins = self.proteins_from_rf(rf)
            for p in proteins:
                res.append(p)
        if ordered:
            return sorted(res, key=len, reverse=True)
        return res

