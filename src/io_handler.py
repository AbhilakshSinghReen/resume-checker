import os


SRC_DIR = os.path.dirname(__file__)
REPO_DIR = os.path.dirname(SRC_DIR)
DATA_DIR = os.path.join(REPO_DIR, "data")
INPUT_FILES_DIR = os.path.join(DATA_DIR, "input-files")


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
