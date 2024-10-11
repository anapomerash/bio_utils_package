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


def transcribe(sequence: str) -> str:
    """
    Транскрибирует ДНК-последовательность в РНК.

    :param sequence: Строка с последовательностью ДНК.
    :return: Транскрибированная последовательность РНК.
    :raises ValueError: Если последовательность содержит 'U'.
    """
    if "U" in sequence.upper():
        raise ValueError("Нельзя транскрибировать РНК-последовательность.")

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
    Разворачивает последовательность.

    :param sequence: Строка с последовательностью.
    :return: Развёрнутая последовательность.
    """
    return sequence[::-1]


def complement(sequence: str) -> str:
    """
    Возвращает комплементарную последовательность.

    :param sequence: Строка с последовательностью ДНК или РНК.
    :return: Комплементарная последовательность.
    :raises ValueError: Если последовательность содержит недопустимые символы.
    """
    if not is_valid_seq(sequence):
        raise ValueError(f"Некорректная последовательность: {sequence}")

    complement_seq = ""
    for nuc in sequence:
        complement_nuc = COMP_DICT.get(nuc, nuc)
        complement_seq += complement_nuc
    return complement_seq


def reverse_complement(sequence: str) -> str:
    """
    Возвращает обратную комплементарную последовательность.

    :param sequence: Строка с последовательностью ДНК или РНК.
    :return: Обратная комплементарная последовательность.
    :raises ValueError: Если последовательность содержит недопустимые символы.
    """
    comp = complement(sequence)
    reverse_comp = comp[::-1]
    return reverse_comp


def is_valid_seq(sequence: str) -> bool:
    """
    Проверяет корректность последовательности нуклеиновых кислот.

    :param sequence: Строка с последовательностью.
    :return: True, если последовательность корректна, иначе False.
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
