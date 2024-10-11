# BioUtils Package

**BioUtils** is a package of bioinformatics utilities for working with nucleic acids and FASTQ sequences.

## Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Working with DNA/RNA](#working-with-DNA-RNA)
  - [FASTQ Filtering](#fastq-filtering)
  - [RNA Translation](#rna-translation)
- [Package Structure](#package-structure)
- [Contacts](#contacts)

## Installation

You can install the package by cloning the repository and installing the necessary dependencies.

```bash
git clone git@github.com:anapomerash/bio_utils_package.git && cd bio_utils_package
```
## Usage

### Working with DNA/RNA

The **run_dna_rna_tools** function allows you to perform various operations on nucleic acid sequences.

```python
from bio_utils import run_dna_rna_tools

# Transcription of DNA to RNA
rna = run_dna_rna_tools('ATG', 'transcribe')
print(rna)  # Output: AUG

# Getting the reverse complement sequence
rev_comp = run_dna_rna_tools('ATG', 'reverse_complement')
print(rev_comp)  # Output: CAT

# Processing multiple sequences
results = run_dna_rna_tools('ATG', 'aT', 'reverse')
print(results)  # Output: ['GTA', 'Ta']

```

### FASTQ Filtering

The **filter_fastq** function filters FASTQ sequences based on specified criteria.

```python
from bio_utils import filter_fastq

# Example data
seqs = {
    "seq1": ("ATGCGT", "IIIIII"),
    "seq2": ("ATGCGU", "!!!!!"),
    "seq3": ("ATGC", "####")
}

# Filtering sequences with GC content between 20% and 80%, length of at least 4, and average quality >= 30
filtered = filter_fastq(seqs, gc_bounds=(20, 80), length_bounds=(4, 100), quality_threshold=30)
print(filtered)
# Output: {'seq1': ('ATGCGT', 'IIIIII')}
```

### RNA Translation

The **translate_rna** function translates an RNA sequence into a chain of amino acids.

```python
from bio_utils import translate_rna

# Example RNA sequence
rna_seq = "AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUUUUAA"

# Translating RNA to amino acid chain
protein = translate_rna(rna_seq)
print(protein)  # Output: MAIVMGR*KGAR*
```

## Package Structure

```python
bio_utils_package/
├── README.md
├── bio_utils.py
├── dna_rna/
│   ├── __init__.py
│   ├── dna_rna_tools.py
├── fastq/
│   ├── __init__.py
│   ├── fastq_utils.py
│   ├── fastq_filtrator_test.py
│   ├── example_data.py
├── translation/
│   ├── __init__.py
│   ├── translation_utils.py
├── flake8.png
└── pytest.png
```

- **bio_utils.py**: Main script containing core functions
- **dna_rna/**: Module for working with DNA/RNA
- **fastq/**: Module for working with FASTQ sequences
- **translation/**: Module for translating RNA into amino acids
- **example_data.py**: Example data for testing
- **flake8.png и pytest.png**: Screenshots of successful linting and testing

## Contacts
If you have any questions or suggestions, please contact us:

anapomerash@gmail.com - Anastasia Pomeranets, Senior Developer
