# translation/translation_utils.py

from typing import Dict

CODON_TABLE: Dict[str, str] = {
    "AUG": "M",  # Start codon
    "UUU": "F",
    "UUC": "F",
    "UUA": "L",
    "UUG": "L",
    "UCU": "S",
    "UCC": "S",
    "UCA": "S",
    "UCG": "S",
    "UAU": "Y",
    "UAC": "Y",
    "UGU": "C",
    "UGC": "C",
    "UGG": "W",
    "CUU": "L",
    "CUC": "L",
    "CUA": "L",
    "CUG": "L",
    "CCU": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CAU": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "CGU": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "AUU": "I",
    "AUC": "I",
    "AUA": "I",
    "ACU": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "AAU": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "AGU": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GUU": "V",
    "GUC": "V",
    "GUA": "V",
    "GUG": "V",
    "GCU": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GAU": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "GGU": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
    # Stop codons
    "UAA": "*",
    "UAG": "*",
    "UGA": "*",
}


def translate_rna(rna_seq: str) -> str:
    """
    Переводит РНК-последовательность в аминокислотную цепь.

    :param rna_seq: Строка с РНК-последовательностью.
    :return: Строка с аминокислотами.
    :raises ValueError: Если последовательность
        содержит недопустимые символы или некорректна.
    """
    if not rna_seq.startswith("AUG"):
        raise ValueError("РНК-последовательность должна начинаться с 'AUG'.")

    protein = ""
    # Проходим по последовательности три нуклеотида за раз
    for i in range(0, len(rna_seq), 3):
        codon = rna_seq[i: i + 3]
        if len(codon) < 3:
            break  # Окончание последовательности
        amino_acid = CODON_TABLE.get(codon.upper(), "X")
        if amino_acid == "*":
            break  # Стоп кодон
        protein += amino_acid
    return protein
