from DNAToolkit import *  # noqa: F403
from utilities import colored
import random

rndDNAStr = "ATTTCGtagT"

#Create a random DNA sequence

randomDNAseq = ''.join([random.choice(Nucleotides) for _ in range(50)])  # noqa: F405

# print(validateSeq(randomDNAseq))  # noqa: F405
# print(countNucFrequency(randomDNAseq))  # noqa: F405
print(f'\nSequence: {colored(randomDNAseq)}\n')
print(f'[1] + Sequence Length: {len(randomDNAseq)}')
print(f'[2] + Nucleotide Frequency: {countNucFrequency(randomDNAseq)}\n')  # noqa: F405
print(f'[3] + DNA/RNA Transcription RNA Sequence: {colored(transcribeDNAtoRNA(randomDNAseq))}\n')  # noqa: F405
print(f"[4] + DNA string + Reverse Complement Sequence:\n5' {colored(randomDNAseq)} 3'")  # noqa: F405
print(f'   {''.join(["|" for _ in range(len(randomDNAseq))])}')
print(f"3  {colored(reverseComplement(randomDNAseq)[::-1])} 5' [Complement]") # noqa: F405
print(f"5' {colored(reverseComplement(randomDNAseq))} 3' [Rev. Complement]\n")  # noqa: F405

print(f'[5] + GC Content: {gc_content(randomDNAseq)}%\n')  # noqa: F405
print(f'[6] + GC Content in Subsection k=5: {gc_content_subseq(randomDNAseq, k=5)}\n') # noqa: F405
print(f'[7] + Protein Translation from DNA Sequence: {translateDNAtoProtein(randomDNAseq, 0)}\n')  # noqa: F405
print(f'[8] + Codon frequency in Protein Translation: {codon_usage(randomDNAseq, "R")}\n')  # noqa: F405