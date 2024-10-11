# bio_utils.py

from .fastq.fastq_utils import filter_fastq
from .translation.translation_utils import translate_rna

__all__ = ["run_dna_rna_tools", "filter_fastq", "translate_rna"]

def run_dna_rna_tools(*args: str) -> Union[str, List[str]]:
    """
    Выполняет указанную процедуру
    над переданными последовательностями ДНК или РНК.

    :param args: Произвольное количество строковых аргументов,
        где последний аргумент — название процедуры.
    :return: Результат выполнения процедуры
        в виде строки или списка строк.
    :raises ValueError: Если последовательность некорректна
        или процедура неизвестна.
    """
    if len(args) < 2:
        raise ValueError(
            """Необходимо передать хотя бы одну последовательность и
            название процедуры."""
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
        raise ValueError(f"Неизвестная процедура: {procedure}")

    for seq in sequences:
        result = functions[procedure](seq)
        results.append(result)

    if len(results) == 1:
        return results[0]
    else:
        return results