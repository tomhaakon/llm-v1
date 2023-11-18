import torch
import pickle
import tarfile
import os
import lzma
import random
#from transformers import GPT2Tokenizer
from tqdm import tqdm
import time
import torch.nn as nn
from torch.nn import functional as F


def read_xz_file(file_path):
    with lzma.open(file_path, 'rt', encoding='utf-8') as file:
        return file.read()
    
def read_all_xz_files(directory):
    texts = []
    for filename in os.listdir(directory):
        if filename.endswith('.xz'):
            file_path = os.path.join(directory, filename)
            file_content = read_xz_file(file_path)
            texts.append(file_content)
    return texts

def process_xz_file(file_path):
    with lzma.open(file_path, 'rt', encoding='utf-8') as file:
        text = file.read()
    # Process the text here (e.g., tokenization, data cleaning)
    # Save or use the processed text before moving to the next file

directory = 'openwebtext/subsets/urlsf_subset02/openwebtext'
for filename in os.listdir(directory):
    if filename.endswith('.xz'):
        file_path = os.path.join(directory, filename)
        process_xz_file(file_path)

def read_xz_files_generator(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.xz'):
            file_path = os.path.join(directory, filename)
            with lzma.open(file_path, 'rt', encoding='utf-8') as file:
                yield file.read()

# Usage
for text in read_xz_files_generator('openwebtext/subsets/urlsf_subset02/openwebtext'):
    # Process each text here

def process_and_save(file_path, output_directory, file_index):
    with lzma.open(file_path, 'rt', encoding='utf-8') as file:
        text = file.read()
    
    # Process the text (add your text processing logic here)
    processed_text = text  # Replace this with actual processing code

    # Save the processed text to a new file
    with open(os.path.join(output_directory, f"processed_{file_index}.txt"), 'w', encoding='utf-8') as out_file:
        out_file.write(processed_text)

output_directory = 'processed_texts'
os.makedirs(output_directory, exist_ok=True)

# Adding tqdm for progress bar
file_list = os.listdir('openwebtext/subsets/urlsf_subset02/openwebtext')
for i, filename in tqdm(enumerate(file_list), total=len(file_list)):
    if filename.endswith('.xz'):
        file_path = os.path.join('openwebtext/subsets/urlsf_subset02/openwebtext', filename)
        process_and_save(file_path, output_directory, i)
