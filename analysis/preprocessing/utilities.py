def colored(seq):
    bcolors ={
            'A': "\033[92m",  # GREEN
            'C': "\033[94m",  # BLUE
            'G': "\033[93m",  # YELLOW
            'T': "\033[91m",  # RED
            'U': "\033[91m",  # RED
            'reset': "\033[0m"  # RESET COLOR
        }
        
    tmpStr = ""
     
    for nucleotide in seq:
        if nucleotide in bcolors:
            tmpStr += bcolors[nucleotide] + nucleotide
        else:
            tmpStr += bcolors['reset'] + nucleotide
    return tmpStr + '\033[0;0m'