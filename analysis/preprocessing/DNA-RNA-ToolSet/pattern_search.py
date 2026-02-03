import re
from time import perf_counter

# loop version
def count_kmer_loops(sequence, kmer):
    """Count occurrences of a k-mer in a sequence using loops."""
    kmer_count = 0
    kmer_length = len(kmer)
    for i in range(len(sequence) - kmer_length + 1):
        if sequence[i:i + kmer_length] == kmer:
            kmer_count += 1
    return kmer_count


# list comprehension version

def count_kmer_list_comp(sequence, kmer):
    kmer_list = [sequence[pos:pos + len(kmer)] for pos in range(len(sequence) - (len(kmer) - 1))]
    return kmer_list.count(kmer)
        
# regex version
def count_kmer_regex(sequence, kmer):
    return len(re.findall(f"(?={kmer})", sequence))

seq = "AAATGCGATATCGATCGAAATCGATCGATCGATCGATCGAAATCGATCG"*1000000
kmer = "AAA"

# testing loop version
start_time = perf_counter()

print("K-mer count using loops:", count_kmer_loops(seq, kmer))

elapsed_time = perf_counter()
execution_time = elapsed_time - start_time

print(f"Execution time (loops): {execution_time:.10f} seconds\n")

# testing list comprehension version
start_time = perf_counter()

print("K-mer count using list_comp:", count_kmer_list_comp(seq, kmer))

elapsed_time = perf_counter()
execution_time = elapsed_time - start_time

print(f"Execution time (list_comp): {execution_time:.10f} seconds\n")

# testing regex version

start_time = perf_counter()

print("K-mer count using regex:", count_kmer_regex(seq, kmer))

elapsed_time = perf_counter()
execution_time = elapsed_time - start_time

print(f"Execution time (lregex): {execution_time:.10f} seconds")





