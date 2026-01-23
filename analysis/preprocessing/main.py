from DNAToolkit import *  # noqa: F403
import random

rndDNAStr = "ATTTCGtagT"

#Create a random DNA sequence

randomDNAseq = ''.join([random.choice(Nucleotides) for _ in range(50)])  # noqa: F405

print(validateSeq(randomDNAseq))  # noqa: F405
print(countNucFrequency(randomDNAseq))  # noqa: F405