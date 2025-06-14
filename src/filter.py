import os
import shutil

from tqdm import tqdm

from src.io_handler import get_outputs, INPUT_FILES_DIR, DATA_DIR


SCORE_THRESHOLD = 2


def main():
    filtered_files_dir = os.path.join(DATA_DIR, "filtered-files")
    os.makedirs(filtered_files_dir, exist_ok=True)

    outputs = get_outputs()
    
    for output in tqdm(outputs):
        score = output['score']
        if score < SCORE_THRESHOLD:
            continue
        
        file_name = output['pdf_name']
        source_file_path = os.path.join(INPUT_FILES_DIR, file_name)
        dest_file_path = os.path.join(filtered_files_dir, file_name)

        shutil.copyfile(source_file_path, dest_file_path)


if __name__ == "__main__":
    main()
