# BioUtils Package

**BioUtils** — это пакет биоинформатических утилит для работы с нуклеиновыми кислотами и FASTQ-сиквенсами.

## Содержание

- [Установка](#установка)
- [Использование](#использование)
  - [Работа с ДНК/РНК](#работа-с-днк-и-рнк)
  - [Фильтрация FASTQ](#фильтрация-fastq)
  - [Трансляция РНК](#трансляция-рнк)
- [Структура пакета](#структура-пакета)
- [Контакты](#контакты)

## Установка

Пакет можно установить, клонировав репозиторий и установив необходимые зависимости.

```bash
git clone git@github.com:anapomerash/bio_utils_package.git
cd bio_utils_package
```
## Использование

### Работа с ДНК/РНК

Функция **run_dna_rna_tools** позволяет выполнять различные операции над нуклеиновыми последовательностями.

```python
from bio_utils import run_dna_rna_tools
# Транскрипция ДНК в РНК
rna = run_dna_rna_tools('ATG', 'transcribe')
print(rna)  # Вывод: AUG

# Получение обратной комплементарной последовательности
rev_comp = run_dna_rna_tools('ATG', 'reverse_complement')
print(rev_comp)  # Вывод: CAT

# Обработка нескольких последовательностей
results = run_dna_rna_tools('ATG', 'aT', 'reverse')
print(results)  # Вывод: ['GTA', 'Ta']
```

### Фильтрация FASTQ

Функция **filter_fastq** фильтрует FASTQ-сиквенсов по заданным критериям.

```python
from bio_utils import filter_fastq

# Пример данных
seqs = {
    "seq1": ("ATGCGT", "IIIIII"),
    "seq2": ("ATGCGU", "!!!!!"),
    "seq3": ("ATGC", "####")
}

# Фильтрация сиквенсов с GC содержанием от 20 до 80%, длиной не менее 4 и средним качеством >= 30
filtered = filter_fastq(seqs, gc_bounds=(20, 80), length_bounds=(4, 100), quality_threshold=30)
print(filtered)
# Вывод: {'seq1': ('ATGCGT', 'IIIIII')}
```

### Трансляция РНК

Функция **translate_rna* позволяет перевести РНК-последовательность в аминокислотную цепь.

```python
from bio_utils import translate_rna

# Пример РНК-последовательности
rna_seq = "AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUUUUAA"

# Трансляция РНК в аминокислотную цепь
protein = translate_rna(rna_seq)
print(protein)  # Вывод: MAIVMGR*KGAR*
```

## Структура пакета

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

- **bio_utils.py**: Главный скрипт с основными функциями
- **dna_rna/**: Модуль для работы с ДНК/РНК
- **fastq/**: Модуль для работы с FASTQ-сиквенсами
- **translation/**: Модуль для трансляции РНК в аминокислоты
- **example_data.py**: Пример данных для тестирования
- **flake8.png и pytest.png**: Скриншоты успешного прохождения проверок

## Контакты
Если у вас возникли вопросы или предложения, пожалуйста, свяжитесь с нами:
anapomerash@gmail.com - Померанец Анастасия, разработчик
