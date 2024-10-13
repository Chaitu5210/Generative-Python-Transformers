import os

file_paths = []

Max_Char_Length = 512
Min_Char_Length = 250

NewLineChar = "<N>"
text_extensions = ['.py']  # Add other text file extensions as needed

# Traverse the directory and collect all file paths
for dirpath, dirnames, filenames in os.walk("Data"):
    for filename in filenames:
        fullpath = os.path.join(dirpath, filename)
        file_paths.append(fullpath)

with open("Python_Data.txt", "a", encoding="utf-8") as output_file:
    for fpath in file_paths:
        # Skip non-text files based on their extension
        if not any(fpath.endswith(ext) for ext in text_extensions):
            continue
        try:
            with open(fpath, "r", encoding="utf-8") as input_file:
                data = input_file.read()
            formatted_data = data.replace("\n", NewLineChar)
            if 100 < len(data) <= Max_Char_Length:
                output_file.write(formatted_data + '\n')
            else:
                splits = formatted_data.split(f"{NewLineChar}{NewLineChar}")
                substring = ""
                for split in splits:
                    substring += split + f"{NewLineChar}{NewLineChar}"
                    if Min_Char_Length <= len(substring) <= Max_Char_Length:
                        output_file.write(substring + '\n')
                        substring = ""
        except FileNotFoundError as e:
            print(f"File not found: {fpath}")
        except UnicodeDecodeError as e:
            print(f"Encoding error processing file {fpath}: {str(e)}")
        except Exception as e:
            print(f"Error processing file {fpath}: {str(e)}")