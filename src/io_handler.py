import os

import fitz
import pandas as pd


SRC_DIR = os.path.dirname(__file__)
REPO_DIR = os.path.dirname(SRC_DIR)
DATA_DIR = os.path.join(REPO_DIR, "data")
INPUT_FILES_DIR = os.path.join(DATA_DIR, "input-files")
OUTPUT_FILE_PATH = os.path.join(DATA_DIR, "output.csv")


def listdir_without_gitkeep(dir_path):
    dir_listing = os.listdir(dir_path)
    if ".gitkeep" in dir_listing:
        dir_listing.remove(".gitkeep")
    
    return dir_listing


def get_input_files():
    file_names = listdir_without_gitkeep(INPUT_FILES_DIR)
    file_paths = [os.path.join(INPUT_FILES_DIR, file_name) for file_name in file_names]
    return file_paths


def get_keywords():
    keywords_file = os.path.join(DATA_DIR, "keywords.txt")
    with open(keywords_file, 'r', encoding="utf-8") as f:
        keywords = f.readlines()
    
    keywords = [keyword.strip() for keyword in keywords]
    keywords = [keyword for keyword in keywords if len(keyword) > 0]
    keywords = list(set(keywords))
    
    return keywords


def pdf_file_to_text(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    
    return text


def add_to_output(input_file_path, score, found_keywords_str):
    row_data = {
        'pdf_name': os.path.basename(input_file_path),
        'score': score,
        'found_keywords_str': found_keywords_str,
    }
    new_row_df = pd.DataFrame([row_data])

    existing_df = pd.read_csv(OUTPUT_FILE_PATH)
    updated_df = pd.concat([existing_df, new_row_df], ignore_index=True)
    updated_df.to_csv(OUTPUT_FILE_PATH, index=False)


def get_outputs():
    df = pd.read_csv(OUTPUT_FILE_PATH)
    return df.to_dict(orient='records')
