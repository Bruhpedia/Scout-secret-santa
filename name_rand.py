import os
import random
import pandas as pd

def secret_santa(input_file_path, output_file_path):
    try:
        _, input_file_extension = os.path.splitext(input_file_path)

        if input_file_extension.lower() == '.txt':
            # If it's a text file, read and write as text
            with open(input_file_path, 'r') as input_file:
                participants = input_file.read().splitlines()

        elif input_file_extension.lower() in ['.xls', '.xlsx']:
            # If it's an Excel file, use pandas to read the data
            df = pd.read_excel(input_file_path)
            participants = df.iloc[:, 0].tolist()

        else:
            print(f"Unsupported file format: {input_file_extension}")
            return

        # Shuffle participants to randomize Secret Santa assignments
        random.shuffle(participants)

        # Create Secret Santa assignments
        assignments = {participants[i]: participants[(i + 1) % len(participants)] for i in range(len(participants))}

        # Write the Secret Santa assignments to the output file
        with open(output_file_path, 'w') as output_file:
            for santa, recipient in assignments.items():
                output_file.write(f"{santa} is the Secret Santa for {recipient}\n")

        print(f"Secret Santa assignments written to '{output_file_path}'.")

    except FileNotFoundError:
        print("Error: The specified files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main module
input_file_path = input("Enter/Copy-paste name of secret santa file: ")
output_file_path = 'secret_santa_assignments.txt'
secret_santa(input_file_path, output_file_path)
