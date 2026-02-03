# import DNAToolkit  as dt 
# from utilities import colored
# import random
# from structures import NM_000207_3, Nucleotides

# # Create a random DNA sequence
# randomDNAseq = ''.join([random.choice(Nucleotides) for _ in range(50)])
# DNAstr = dt.validateSeq(randomDNAseq)
# print(validateSeq(randomDNAseq))
# print(countNucFrequency(randomDNAseq))
# print(f'\nSequence: {colored(randomDNAseq)}\n')
# print(f'[1] + Sequence Length: {len(randomDNAseq)}')
# print(f'[2] + Nucleotide Frequency: {dt.countNucFrequency(randomDNAseq)}\n')
# print(f'[3] + DNA/RNA Transcription RNA Sequence: {colored(dt.transcribeDNAtoRNA(randomDNAseq))}\n') 
# print(f"[4] + DNA string + Reverse Complement Sequence:\n5' {colored(randomDNAseq)} 3'")
# print(f'   {''.join(["|" for _ in range(len(randomDNAseq))])}')
# print(f"3  {colored(dt.reverseComplement(randomDNAseq)[::-1])} 5' [Complement]")
# print(f"5' {colored(dt.reverseComplement(randomDNAseq))} 3' [Rev. Complement]\n")
# print(f'[5] + GC Content: {dt.gc_content(randomDNAseq)}%\n')
# print(f'[6] + GC Content in Subsection k=5: {dt.gc_content_subseq(randomDNAseq, k=5)}\n')
# print(f'[7] + Protein Translation from DNA Sequence: {dt.translateDNAtoProtein(randomDNAseq, 0)}\n')
# print(f'[8] + Codon frequency in Protein Translation: {dt.codon_usage(randomDNAseq, "R")}\n')
# print('[9] + Reading frames:\n')
# for frame in dt.gen_reading_frames(randomDNAseq):
#     print (frame)  
# test_rf_frame = ["L","M","T","A","L","V","V","L","V","R","R","G","S","_","G","H"]
# print(dt.proteins_from_rf(test_rf_frame)) 
# print('\n[10] + Proteins from all 6 Reading Frames:\n')
# for prot in dt.all_proteins_from_orfs(NM_000207_3, 0, 0, True): 
#     print(f'{colored(prot)}')



# The line `from bio_seq import bio_seq` is importing the `bio_seq` class from the `bio_seq` module.
# This allows you to use the `bio_seq` class in your current Python script.
from bio_seq import bio_seq
from utilities import writeTextFile


test_DNA = bio_seq()
test_DNA.generate_random_seq(length=100, seq_type="RNA")
print(test_DNA.get_seq_info())
print(test_DNA.countNucFrequency())
print(test_DNA.transcribeDNAtoRNA())
print(test_DNA.reverseComplement())
print(test_DNA.gc_content())
print(test_DNA.gc_content_subseq(k=5))
print(test_DNA.codon_usage("L"))

for frame in test_DNA.gen_reading_frames():
    print(frame)
print(test_DNA.all_proteins_from_orfs())

writeTextFile("test_sequence.txt", test_DNA.seq)

for frame in test_DNA.gen_reading_frames():
    writeTextFile("test_sequence.txt", str(frame), 'a')