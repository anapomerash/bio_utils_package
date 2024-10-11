import os
import sys


def convert_multiline_fasta_to_oneline(input_fasta: str, output_fasta: str) -> None:
    """
    Converts a multi-line FASTA file into a single-line FASTA file.

    :param input_fasta: Path to the input FASTA file.
    :param output_fasta: Path to the output FASTA file.
    """
    output_dir = os.path.dirname(output_fasta)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    with open(input_fasta, "r") as infile, open(output_fasta, "w") as outfile:
        for line in infile:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                outfile.write(f"{line}\n")
            else:
                outfile.write(f"{line}")
        outfile.write("\n")


def parse_blast_output(input_file: str, output_file: str) -> None:
    """
    Parses BLAST output to extract unique protein names and saves them sorted alphabetically.

    :param input_file: Path to the input BLAST output file (txt format).
    :param output_file: Path to the output file to save the results.
    """
    proteins = set()
    capture = False

    with open(input_file, "r") as infile:
        for line in infile:
            if "Sequences producing significant alignments:" in line:
                capture = True
                next(infile, None)
                continue
            if capture:
                line = line.strip()
                if not line:
                    break
                parts = line.split("\t")
                if len(parts) >= 2:
                    proteins.add(parts[1])

    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    with open(output_file, "w") as outfile:
        for protein in sorted(proteins):
            outfile.write(f"{protein}\n")


def main():
    """
    Main function to process command-line arguments and execute the appropriate function.
    """
    if len(sys.argv) != 4:
        print("Usage:")
        print(
            "  To convert FASTA: python bio_files_processor.py convert example_data/example_multiline_fasta.fasta filtered/output_oneline.fasta"
        )
        print(
            "  To parse BLAST: python bio_files_processor.py parse example_data/example_blast_results.txt filtered/blast_parsed.txt"
        )
        sys.exit(1)

    action = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    if action == "convert":
        convert_multiline_fasta_to_oneline(input_file, output_file)
        print(f"Converted {input_file} to {output_file} successfully.")
    elif action == "parse":
        parse_blast_output(input_file, output_file)
        print(
            f"Parsed BLAST output from {input_file} and saved to {output_file} successfully."
        )
    else:
        print(f"Unknown action: {action}")
        print("Available actions: convert, parse")
        sys.exit(1)


if __name__ == "__main__":
    main()
