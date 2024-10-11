from typing import List, Union

COMP_DICT = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G",
    "U": "A",
    "a": "t",
    "t": "a",
    "g": "c",
    "c": "g",
    "u": "a",
}


def transcribe(sequence: str) -> str:
    """
    Transcribes a DNA sequence into RNA.

    :param sequence: A string representing the DNA sequence.
    :return: The transcribed RNA sequence.
    :raises ValueError: If the sequence contains 'U'.
    """
    if "U" in sequence.upper():
        raise ValueError("Cannot transcribe an RNA sequence.")

    transcribed = ""
    for nucleotide in sequence:
        if nucleotide == "T":
            transcribed += "U"
        elif nucleotide == "t":
            transcribed += "u"
        else:
            transcribed += nucleotide
    return transcribed


def reverse(sequence: str) -> str:
    """
    Reverses the given sequence.

    :param sequence: A string representing the sequence.
    :return: The reversed sequence.
    """
    return sequence[::-1]


def complement(sequence: str) -> str:
    """
    Returns the complementary sequence.

    :param sequence: A string representing the DNA or RNA sequence.
    :return: The complementary sequence.
    :raises ValueError: If the sequence contains invalid characters.
    """
    if not is_valid_seq(sequence):
        raise ValueError(f"Invalid sequence: {sequence}")

    complement_seq = ""
    for nuc in sequence:
        complement_nuc = COMP_DICT.get(nuc, nuc)
        complement_seq += complement_nuc
    return complement_seq


def reverse_complement(sequence: str) -> str:
    """
    Returns the reverse complementary sequence.

    :param sequence: A string representing the DNA or RNA sequence.
    :return: The reverse complementary sequence.
    :raises ValueError: If the sequence contains invalid characters.
    """
    return reverse(complement(sequence))


def is_valid_seq(sequence: str) -> bool:
    """
    Checks the validity of a nucleotide sequence.

    :param sequence: A string representing the sequence.
    :return: True if the sequence is valid, otherwise False.
    """
    dna_bases = set("ATGCatgc")
    rna_bases = set("AUGCaugc")
    sequence_set = set(sequence)

    if sequence_set <= dna_bases:
        return True
    elif sequence_set <= rna_bases:
        return True
    else:
        return False