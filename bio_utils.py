from typing import List, Union
from fastq.fastq_utils import filter_fastq
from translation.translation_utils import translate_rna
from dna_rna.dna_rna_tools import transcribe, reverse, complement, reverse_complement

__all__ = ["run_dna_rna_tools", "filter_fastq", "translate_rna"]

def run_dna_rna_tools(*args: str) -> Union[str, List[str]]:
    """
    Executes the specified procedure on the provided DNA or RNA sequences.

    :param args: Variable number of string arguments,
                 where the last argument is the name of the procedure.
    :return: The result of the procedure as a string or a list of strings.
    :raises ValueError: If the sequence is invalid or the procedure is unknown.
    """
    if len(args) < 2:
        raise ValueError(
            "At least one sequence and the name of the procedure must be provided."
        )

    procedure = args[-1]
    sequences = args[:-1]
    results = []

    functions = {
        "transcribe": transcribe,
        "reverse": reverse,
        "complement": complement,
        "reverse_complement": reverse_complement,
    }

    if procedure not in functions:
        raise ValueError(f"Unknown procedure: {procedure}")

    for seq in sequences:
        result = functions[procedure](seq)
        results.append(result)

    if len(results) == 1:
        return results[0]
    else:
        return results