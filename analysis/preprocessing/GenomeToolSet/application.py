from GenomeToolkit import genomeToolkit

gt = genomeToolkit()

seq = "AAATGCGTACGTAGCTAAAGCTAAGCTAAAGCTAGCTA"
kmer = "AAA"

print(f"Sequence: {seq}")
print(f"K-mer: {kmer}")
print(f"Repeats found: {gt.count_kmer(seq, kmer)}")