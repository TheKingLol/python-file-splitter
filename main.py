import os
import shutil
from tqdm import tqdm

def split_text_file(input_file, output_dir, max_size):
    file_num = 1
    current_size = 0

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_name = os.path.splitext(os.path.basename(input_file))[0]  # Get the base name of the input file

    with open(input_file, 'r') as infile:
        output_file = open(os.path.join(output_dir, f"{file_name}_{file_num}.txt"), 'w')
        pbar = tqdm(total=max_size, unit='B', unit_scale=True)

        for line in infile:
            output_file.write(line)
            current_size += len(line)
            pbar.update(len(line))

            if current_size >= max_size:
                output_file.close()
                file_num += 1
                current_size = 0
                pbar.close()
                output_file = open(os.path.join(output_dir, f"{file_name}_{file_num}.txt"), 'w')
                pbar = tqdm(total=max_size, unit='B', unit_scale=True)

        pbar.close()

if __name__ == "__main__":
    input_file = input("Enter the path of the input file: ")  # Prompt the user for the input file path
    output_dir = "out"  # Output directory
    max_size_mb = float(input("Enter the maximum file size (in MB): "))  # Prompt the user for the maximum file size in MB

    max_size = int(max_size_mb * 1024 * 1024)  # Convert MB to bytes

    split_text_file(input_file, output_dir, max_size)

