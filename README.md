# BioUtils Package

**BioUtils** — is a bioinformatics utilities package designed for working with nucleic acids and FASTQ sequences.

## Contents

-   [Installation](#installation)
-   [Usage](#usage)
    -   [DNA/RNA Tools](#dna-rna-tools)
    -   [FASTQ Filtering](#fastq-filtering)
    -   [RNA Translation](#rna-translation)
    -   [Bioinformatics File Processing](#bioinformatics-file-processing)
-   [Package Structure](#package-structure)
-   [Contacts](#contacts)

## Installation {#installation}

You can install the package by cloning the repository and setting up the necessary dependencies.

``` bash
git clone git@github.com:anapomerash/bio_utils_package.git && cd bio_utils_package
```

## Usage {#usage}

### DNA/RNA Tools

The **run_dna_rna_tools function** allows you to perform various operations on nucleotide sequences.

``` python
from bio_utils import run_dna_rna_tools

# Transcribe DNA to RNA
rna = run_dna_rna_tools('ATG', 'transcribe')
print(rna)  # Output: AUG

# Get reverse complement of DNA
rev_comp = run_dna_rna_tools('ATG', 'reverse_complement')
print(rev_comp)  # Output: CAT

# Process multiple sequences
results = run_dna_rna_tools('ATG', 'aT', 'reverse')
print(results)  # Output: ['GTA', 'Ta']
```

### FASTQ Filtering {#fastq-filtering}

The **filter_fastq** function filters FASTQ sequences based on specified criteria.

#### Filtering Example

``` python
from bio_utils import filter_fastq

# Define input and output FASTQ file paths
input_fastq = 'example_data/example_fastq.fastq'
output_fastq = 'filtered/output.fastq'

# Filter sequences with GC content between 20-80%, length between 50-1000, and average quality >= 30
filter_fastq(
    input_fastq=input_fastq,
    output_fastq=output_fastq,
    gc_bounds=(20, 80),
    length_bounds=(50, 1000),
    quality_threshold=30
)

print("FASTQ filtering completed. Filtered sequences saved to 'filtered/output.fastq'.")
```

#### Expected Output (**filtered/output.fastq**):

```         
@SRX079804:1:SRR292678:1:1101:21885:21885 1:N:0:1 BH:ok
ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA
+SRX079804:1:SRR292678:1:1101:21885:21885 1:N:0:1 BH:ok
FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD
@SRX079804:1:SRR292678:1:1101:105156:105156 1:N:0:1 BH:ok
ACTGCTGAGCTTAAATGGCGGCAGTCTGACGGTTACCAACGGGGGCACTTCAACCGGTTCGTTAACGGGGAGCGGAGAGCTGA
+SRX079804:1:SRR292678:1:1101:105156:105156 1:N:0:1 BH:ok
GFFEGGFGGGGEGGGGGGGGGFDD=DDE7EDD6CD?FEDEE@EBEFEE.DD5DDD@B<7>/0543C?BEE?@@BE<B?/B>@;
```

Only sequences that meet the specified criteria are included in the output.

### RNA Translation

The **translate_rna** function translates an RNA sequence into an amino acid chain.


``` python
from bio_utils import translate_rna

# Пример РНК-последовательности
rna_seq = "AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUUUUAA"

# Трансляция РНК в аминокислотную цепь
protein = translate_rna(rna_seq)
print(protein)  # Вывод: MAIVMGR*KGAR*
```

## Bioinformatics File Processing

The **bio_files_processor.py** script contains functions for processing various bioinformatics files, such as converting FASTA files and parsing BLAST output.

### Convert Multiline FASTA to Oneline FASTA

Converts a multi-line FASTA file into a single-line FASTA file.

``` bash
python bio_files_processor.py convert example_data/example_multiline_fasta.fasta filtered/output_oneline.fasta
``` 

### Expected Output:

``` bash
Created directory: filtered
Converted example_data/example_multiline_fasta.fasta to filtered/output_oneline.fasta successfully.
``` 

### Parse BLAST Output

Parses a BLAST output file to extract unique protein names and saves them sorted alphabetically.

``` bash
python bio_files_processor.py parse example_data/example_blast_results.txt filtered/blast_parsed.txt
``` 
### Expected Output:

``` bash
Created directory: filtered
Parsed BLAST output from example_data/example_blast_results.txt and saved to filtered/blast_parsed.txt successfully.
``` 
## Package Structure

``` python
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
├── bio_files_processor.py
├── example_data/
│   ├── example_fastq.fastq
│   ├── example_blast_results.txt
│   ├── example_multiline_fasta.fasta
│   ├── example_gbk.gbk
├── filtered/
│   ├── output.fastq
│   ├── blast_parsed.txt
│   ├── output_oneline.fasta
│   ├── selected_genes.fasta
├── .gitignore
├── flake8.png
└── pytest.png
```

-   **bio_utils.py**: Main script containing core functions
-   **dna_rna/**: Module for DNA/RNA operations
-   **fastq/**: Module for handling FASTQ sequences
-   **translation/**: Module for RNA translation
-   **bio_files_processor.py**: Script for processing bioinformatics files (FASTA conversion, BLAST parsing)
-   **example_data/**: Sample input data for testing.
-   **filtered/**: Directory for storing filtered and processed data

## Contacts

If you have any questions or suggestions, please contact us:

anapomerash@gmail.com - Anastasia Pomerash, Senior Developer