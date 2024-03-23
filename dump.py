import os

def dump_python_files(directory, output_file):
    with open(output_file, 'w') as outfile:
        # Walk through the directory
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Check if the file is a Python file
                if file.endswith('.py'):
                    module_name = os.path.splitext(file)[0]
                    outfile.write(f"Module: {module_name}\n\n")

                    # Construct the full file path
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as infile:
                        # Write the content of the file to the output file
                        outfile.write(infile.read())

                    # Add a separator between files
                    outfile.write("\n\n" + "#" * 80 + "\n\n")

# Usage example
directory_path = './server'
output_file_path = 'sasa.txt'  # The file will be created in the current directory
dump_python_files(directory_path, output_file_path)
