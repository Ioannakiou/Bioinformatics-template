from GenomeToolkit import genomeToolkit

gt = genomeToolkit()

seq = "AAATGCAAA"
kmer = "AAA"
k_len = 3

print(f"Sequence: {seq}")
print(f"K-mer: {kmer}")
# print(f"Repeats found: {gt.count_kmer(seq, kmer)}")
print(f"Most frequent k-mers: {gt.find_most_frequent_kmers(seq, k_len)}")