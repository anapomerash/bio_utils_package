import os
from typing import Tuple, Union

def calculate_gc_content(sequence: str) -> float:
    """
    Calculates the GC content percentage of a nucleotide sequence.

    :param sequence: A string representing the nucleotide sequence.
    :return: GC content as a percentage.
    """
    if not sequence:
        return 0.0
    gc_count = sum(1 for nuc in sequence.upper() if nuc in ('G', 'C'))
    return (gc_count / len(sequence)) * 100

def calculate_avg_quality(quality: str) -> float:
    """
    Calculates the average quality score of a FASTQ sequence using Phred33 encoding.

    :param quality: A string representing the quality scores.
    :return: Average quality score.
    """
    if not quality:
        return 0.0
    quality_scores = [phred_score(char) for char in quality]
    return sum(quality_scores) / len(quality_scores)

def phred_score(char: str) -> int:
    """
    Converts a Phred33 character to its corresponding quality score.

    :param char: A single character representing the quality score.
    :return: Numerical quality score.
    """
    phred_mapping = {
        "!": 0, '"': 1, "#": 2, "$": 3, "%": 4, "&": 5, "'": 6, "(": 7, ")": 8,
        "*": 9, "+": 10, ",": 11, "-": 12, ".": 13, "/": 14, "0": 15, "1": 16,
        "2": 17, "3": 18, "4": 19, "5": 20, "6": 21, "7": 22, "8": 23, "9": 24,
        ":": 25, ";": 26, "<": 27, "=": 28, ">": 29, "?": 30, "@": 31, "A": 32,
        "B": 33, "C": 34, "D": 35, "E": 36, "F": 37, "G": 38, "H": 39, "I": 40,
        "J": 41, "K": 42, "L": 43, "M": 44, "N": 45, "O": 46, "P": 47, "Q": 48,
        "R": 49, "S": 50, "T": 51, "U": 52, "V": 53, "W": 54, "X": 55, "Y": 56,
        "Z": 57, "[": 58, "\\": 59, "]": 60, "^": 61, "_": 62, "`": 63, "a": 64,
        "b": 65, "c": 66, "d": 67, "e": 68, "f": 69, "g": 70, "h": 71, "i": 72,
        "j": 73, "k": 74, "l": 75, "m": 76, "n": 77, "o": 78, "p": 79, "q": 80,
        "r": 81, "s": 82, "t": 83, "u": 84, "v": 85, "w": 86, "x": 87, "y": 88,
        "z": 89, "{": 90, "|": 91, "}": 92, "~": 93,
    }
    return phred_mapping.get(char, 0)

def is_within_bounds(
    value: Union[float, int],
    bounds: Union[
        Tuple[Union[float, int], Union[float, int]],
        Union[float, int],
    ],
) -> bool:
    """
    Checks if a value is within specified bounds.

    :param value: The value to check.
    :param bounds: A tuple specifying (lower, upper) bounds or a single upper bound.
    :return: True if within bounds, else False.
    """
    if isinstance(bounds, tuple):
        lower, upper = bounds
        return lower <= value <= upper
    else:
        return value <= bounds

def filter_fastq(
    input_fastq: str,
    output_fastq: str,
    gc_bounds: Union[Tuple[float, float], float] = (0, 100),
    length_bounds: Union[Tuple[int, int], int] = (0, 2**32),
    quality_threshold: float = 0.0,
) -> None:
    """
    Filters FASTQ sequences from an input file based on specified criteria and writes the filtered sequences to an output file.

    :param input_fastq: Path to the input FASTQ file.
    :param output_fastq: Path to the output FASTQ file.
    :param gc_bounds: Tuple specifying (min, max) GC content percentage or a single upper bound.
    :param length_bounds: Tuple specifying (min, max) sequence length or a single upper bound.
    :param quality_threshold: Minimum average quality score required.
    """
    output_dir = os.path.dirname(output_fastq)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(input_fastq, 'r') as infile, open(output_fastq, 'w') as outfile:
        while True:
            header = infile.readline().strip()
            if not header:
                break
            sequence = infile.readline().strip()
            plus = infile.readline().strip()
            quality = infile.readline().strip()

            gc_content = calculate_gc_content(sequence)
            length = len(sequence)
            avg_quality = calculate_avg_quality(quality)

            if (
                is_within_bounds(gc_content, gc_bounds) and
                is_within_bounds(length, length_bounds) and
                avg_quality >= quality_threshold
            ):
                outfile.write(f"{header}\n{sequence}\n{plus}\n{quality}\n")