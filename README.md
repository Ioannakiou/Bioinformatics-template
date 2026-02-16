# Bioinformatics Analysis Template

A collection of Python scripts developed while studying a bioinformatics course. This repository documents my learning journey through core bioinformatics concepts, including DNA/RNA sequence analysis, genome preprocessing, protein translation, and k-mer pattern search.

---

## 📁 Repository Structure

```
Bioinformatics-template/
├── analysis/
│   └── preprocessing/
│       ├── DNA-RNA-ToolSet/
│       │   ├── bio_seq.py          # OOP bio sequence class with full toolkit
│       │   ├── bio_structs.py      # Nucleotide/codon lookup tables (DNA & RNA)
│       │   ├── DNAToolkit.py       # Functional-style DNA analysis utilities
│       │   ├── hamming_distance.py # Sequence similarity via Hamming distance
│       │   ├── main.py             # Entry point / usage examples
│       │   ├── pattern_search.py   # K-mer counting & benchmarking
│       │   ├── structures.py       # Core data structures and a real gene sequence
│       │   └── utilities.py        # I/O helpers and colour-coded terminal output
│       └── GenomeToolSet/
│           ├── GenomeToolkit.py    # OOP genome toolkit class
│           └── application.py      # Entry point / usage examples
├── .github/                        # GitHub Actions workflows and templates
├── .vscode/                        # VS Code workspace settings
├── .gitignore
└── README.md
```

---

## 🔬 Analyses Included

### 1. DNA & RNA Sequence Processing (`bio_seq.py`, `DNAToolkit.py`)

The core of the toolkit. Implemented in both an object-oriented style (`bio_seq` class) and as standalone functions (`DNAToolkit.py`), covering:

- **Sequence validation** — checks that a sequence contains only valid nucleotides for its type (DNA or RNA)
- **Nucleotide frequency counting** — tallies occurrences of A, T/U, C, G
- **DNA → RNA transcription** — replaces thymine (T) with uracil (U)
- **Reverse complement** — computes the reverse complement for both DNA and RNA strands
- **GC content** — calculates overall GC% and GC% across sliding subsequence windows of length _k_
- **DNA/RNA → protein translation** — converts codons to amino acids using full codon tables
- **Codon usage analysis** — calculates the relative frequency of synonymous codons for a given amino acid
- **Reading frame generation** — produces all 6 reading frames (3 forward + 3 reverse complement)
- **Open reading frame (ORF) extraction** — identifies all possible proteins from all reading frames, with optional length-ordered output
- **Random sequence generation** — generates random DNA or RNA sequences of a specified length

### 2. Hamming Distance (`hamming_distance.py`)

Compares two DNA sequences of equal length to quantify their similarity. Three implementations are provided and compared:

- **Loop-based** — classic positional iteration
- **Set-based** — uses set difference on enumerated nucleotide pairs
- **Zip-based** — Pythonic one-liner using `zip()`

Useful for mutation analysis and evaluating sequence divergence.

### 3. K-mer / Pattern Search (`pattern_search.py`)

Counts occurrences of a sub-sequence (k-mer) within a larger DNA sequence. Three approaches are benchmarked against each other using `time.perf_counter`:

- **Loop** — sliding window character-by-character comparison
- **List comprehension** — generates all k-mers then counts matches
- **Regex** — uses lookahead (`(?=...)`) to handle overlapping matches

This module is useful for motif discovery and evaluating performance trade-offs at scale.

### 4. Biological Data Structures (`bio_structs.py`, `structures.py`)

Lookup tables and reference data used across the toolkit:

- `NUCLEOTIDE_BASE` — valid bases for DNA (`A T C G`) and RNA (`A U C G`)
- `DNA_Codons` / `RNA_Codons` — full 64-codon translation tables mapping triplets to amino acids (including START `M` and STOP `_`)
- `DNA_Reverse_Comp` — nucleotide complement mapping
- `NM_000207_3` — a real reference sequence for the human insulin gene (*INS*), sourced from NCBI, used for ORF and protein extraction examples

### 5. Genome K-mer Analysis (`GenomeToolkit.py`)

A dedicated object-oriented toolkit for genome-level sequence analysis, implemented as the `genomeToolkit` class:

- **K-mer counting with overlap** — counts all occurrences of a given k-mer within a sequence, correctly handling overlapping matches. For example, searching for `AAA` in `AAAATGC` counts both positions at index 0 and 1, rather than skipping ahead by _k_.

Run from the `GenomeToolSet/` directory:

```bash
cd analysis/preprocessing/GenomeToolSet
python application.py
```

Example output:
```
Sequence: AAATGCGTACGTAGCTAAAGCTAAGCTAAAGCTAGCTA
K-mer: AAA
Repeats found: 3
```

### 6. Utilities (`utilities.py`)

Helper functions for I/O and visualisation:

- **`colored(seq)`** — prints nucleotide sequences in colour-coded terminal output (A=green, C=blue, G=yellow, T/U=red)
- **`readTextFile(path)`** — reads a sequence from a plain text file
- **`writeTextFile(path, seq)`** — writes or appends a sequence to a plain text file

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/) or [conda](https://docs.conda.io/en/latest/)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Ioannakiou/Bioinformatics-template.git
   cd Bioinformatics-template
   ```

2. **Create and activate a virtual environment** (recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   No external dependencies are required — the toolkit uses Python's standard library only.

---

## ▶️ Usage

**DNA-RNA-ToolSet** — run the main entry point to see the full toolkit in action on a randomly generated RNA sequence:

```bash
cd analysis/preprocessing/DNA-RNA-ToolSet
python main.py
```

Or use the `bio_seq` class directly in your own scripts:

```python
from bio_seq import bio_seq

seq = bio_seq("ATGCGATACGCTTACGCT", "DNA", "My gene")
print(seq.gc_content())           # GC content %
print(seq.transcribeDNAtoRNA())   # Transcribe to RNA
print(seq.all_proteins_from_orfs(ordered=True))  # Extract proteins from all ORFs
```

**GenomeToolSet** — run k-mer analysis on a genome sequence:

```bash
cd analysis/preprocessing/GenomeToolSet
python application.py
```

Or use the `genomeToolkit` class directly:

```python
from GenomeToolkit import genomeToolkit

gt = genomeToolkit()
print(gt.count_kmer("AAATGCGTACGTAGCTAAAGCTA", "AAA"))  # Count overlapping k-mers
```

---

## 🛠️ Development Setup

This template includes VS Code settings (`.vscode/`) for a consistent development experience. Recommended extensions:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

---

## 📚 About This Project

The scripts in this repository were produced as part of a bioinformatics course and are intended as a learning reference. They cover foundational bioinformatics programming concepts implemented from scratch in Python.

---
