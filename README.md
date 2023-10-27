# Text File Splitter

## Description

The Text File Splitter is a Python script that allows users to split large text files into smaller, more manageable parts without cutting off lines. It provides an easy way to process and work with large text-based datasets.

## Features

- Split large text files into smaller parts.
- Specify the maximum file size in megabytes for the split parts.
- Maintain the integrity of lines in the original text file.
- Display a progress bar during the splitting process.

## Getting Started

### Prerequisites

- Python 3.x (tested on Python 3.6 and later)

### Installation

1. Clone this repository or download the script to your local machine.

2. Install the required packages

    ```pip install -r requirements.txt```

### Usage
1. Run the script from the command line:

    ```python3 main.py```
    
2. Follow the on-screen prompts:

- Enter the path of the text file
- Specify the maximum file size for the split parts in megabytes

3. The script will create an output directory and split the input file into smaller files. The output files will be named after the input file with numerical suffixes (e.g., input_file_1.txt, input_file_2.txt, etc.).

### Example

Here's an example of the script in action

```
$ python split_text_file.py
Enter the path of the input file: large_data.txt
Enter the maximum file size (in MB): 10
```

### Licence

This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments

The script uses the tqdm library for displaying a progress bar.
