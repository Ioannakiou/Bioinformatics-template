def colored(seq):
    bcolors ={
            'A': "\033[92m",  # GREEN
            'C': "\033[94m",  # BLUE
            'G': "\033[93m",  # YELLOW
            'T': "\033[91m",  # RED
            'U': "\033[91m",  # RED
            'reset': "\033[0m"  # RESET COLOR
        }
        
    result = "".join(
        bcolors[nucleotide] + nucleotide if nucleotide in bcolors else bcolors['reset'] + nucleotide
        for nucleotide in seq
    )
    return result + '\033[0;0m'

def readTextFile(filePath):
    with open(filePath, 'r') as f:
        return "".join([l.strip() for l in f.readlines()])  # noqa: E741
    
def writeTextFile(filePath, seq, mode='w'):
    with open(filePath, mode) as f:
        f.write(seq + '\n')