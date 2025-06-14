from tqdm import tqdm

from src.io_handler import get_input_files, get_keywords, pdf_file_to_text, add_to_output
from src.matching import search_keywords_in_text


def main():
    input_files = get_input_files()
    keywords = get_keywords()
    
    for input_file_path in tqdm(input_files):
        pdf_text = pdf_file_to_text(input_file_path)
        found_keywords = search_keywords_in_text(pdf_text, keywords, True)

        score = len(found_keywords)
        found_keywords_str = "; ".join(found_keywords)

        add_to_output(input_file_path, score, found_keywords_str)


if __name__ == "__main__":
    main()
