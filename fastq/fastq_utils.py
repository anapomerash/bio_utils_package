from typing import Dict, Tuple, Union


def filter_fastq(
    seqs: Dict[str, Tuple[str, str]],
    gc_bounds: Union[Tuple[float, float], float] = (0, 100),
    length_bounds: Union[Tuple[int, int], int] = (0, 2**32),
    quality_threshold: float = 0.0,
) -> Dict[str, Tuple[str, str]]:
    """
    Фильтрует FASTQ-сиквенсы по заданным критериям.

    :param seqs: Словарь с FASTQ-сиквенсами.
        Ключ - имя последовательности,
        значение - кортеж (последовательность, качество).
    :param gc_bounds: Интервал GC-содержания (в процентах).
        Если одно число, то верхняя граница.
    :param length_bounds: Интервал длины последовательности.
        Если одно число, то верхняя граница.
    :param quality_threshold: Порог среднего качества последовательности.
    :return: Отфильтрованный словарь с сиквенсами,
        удовлетворяющими всем условиям.
    """
    filtered_seqs = {}

    for name, (sequence, quality) in seqs.items():
        gc_content = calculate_gc_content(sequence)
        length = len(sequence)
        avg_quality = calculate_avg_quality(quality)

        if not is_within_bounds(gc_content, gc_bounds):
            continue
        if not is_within_bounds(length, length_bounds):
            continue
        if avg_quality < quality_threshold:
            continue

        filtered_seqs[name] = (sequence, quality)

    return filtered_seqs


def calculate_gc_content(sequence: str) -> float:
    """
    Вычисляет процентное содержание GC в последовательности.

    :param sequence: Строка с нуклеотидной последовательностью.
    :return: Процентное содержание GC.
    """
    if not sequence:
        return 0.0
    gc_count = 0
    for nuc in sequence.upper():
        if nuc == "G" or nuc == "C":
            gc_count += 1
    gc_content = (gc_count / len(sequence)) * 100
    return gc_content


def calculate_avg_quality(quality: str) -> float:
    """
    Вычисляет среднее качество сиквенса по шкале Phred33.

    :param quality: Строка с качеством каждого нуклеотида.
    :return: Среднее качество.
    """
    if not quality:
        return 0.0
    quality_scores = []
    for char in quality:
        score = phred_score(char)
        quality_scores.append(score)
    avg_quality = sum(quality_scores) / len(quality_scores)
    return avg_quality


def phred_score(char: str) -> int:
    """
    Преобразует символ качества в числовое значение по шкале Phred33.

    :param char: Символ качества.
    :return: Числовое значение качества.
    """
    phred_mapping = {
        "!": 0,
        '"': 1,
        "#": 2,
        "$": 3,
        "%": 4,
        "&": 5,
        "'": 6,
        "(": 7,
        ")": 8,
        "*": 9,
        "+": 10,
        ",": 11,
        "-": 12,
        ".": 13,
        "/": 14,
        "0": 15,
        "1": 16,
        "2": 17,
        "3": 18,
        "4": 19,
        "5": 20,
        "6": 21,
        "7": 22,
        "8": 23,
        "9": 24,
        ":": 25,
        ";": 26,
        "<": 27,
        "=": 28,
        ">": 29,
        "?": 30,
        "@": 31,
        "A": 32,
        "B": 33,
        "C": 34,
        "D": 35,
        "E": 36,
        "F": 37,
        "G": 38,
        "H": 39,
        "I": 40,
        "J": 41,
        "K": 42,
        "L": 43,
        "M": 44,
        "N": 45,
        "O": 46,
        "P": 47,
        "Q": 48,
        "R": 49,
        "S": 50,
        "T": 51,
        "U": 52,
        "V": 53,
        "W": 54,
        "X": 55,
        "Y": 56,
        "Z": 57,
        "[": 58,
        "\\": 59,
        "]": 60,
        "^": 61,
        "_": 62,
        "`": 63,
        "a": 64,
        "b": 65,
        "c": 66,
        "d": 67,
        "e": 68,
        "f": 69,
        "g": 70,
        "h": 71,
        "i": 72,
        "j": 73,
        "k": 74,
        "l": 75,
        "m": 76,
        "n": 77,
        "o": 78,
        "p": 79,
        "q": 80,
        "r": 81,
        "s": 82,
        "t": 83,
        "u": 84,
        "v": 85,
        "w": 86,
        "x": 87,
        "y": 88,
        "z": 89,
        "{": 90,
        "|": 91,
        "}": 92,
        "~": 93,
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
    Проверяет, находится ли значение в заданных границах.

    :param value: Значение для проверки.
    :param bounds: Границы.
        Кортеж из двух значений или одно число.
    :return: True, если значение в границах, иначе False.
    """
    if isinstance(bounds, tuple):
        lower, upper = bounds
        return lower <= value <= upper
    else:
        return value <= bounds
