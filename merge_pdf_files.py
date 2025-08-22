from pypdf import PdfWriter
import sys


def pdf_combiner(file_list, out_path):
    merger = PdfWriter()
    for pdf in file_list:
        merger.append(pdf)
    with open(out_path, "wb") as envelope:
        merger.write(envelope)
    merger.close()


if __name__ == "__main__":
    try:
        new_envelope = sys.argv[1]
        files = sys.argv[2:]
        pdf_combiner(files, new_envelope)
        print(f"Wrote the output file: {new_envelope}")
    except Exception as err:
        print(f"Error: {err}")
        print(
            "Usage: python3 merge_pdf_files.py <output_file.pdf> <input_file_1.pdf> <input_file_2.pdf>"
        )
