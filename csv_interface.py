import pandas as pd
import os

def load_results(csv_path):
    return pd.read_csv(csv_path)

def display_report(df):
    print("Available Reports:")
    print("\t1. Show all entries")
    print("\t2. Show specific entry")
    choice = input("Enter choice: ")
    
    if choice == '1':
        print(df)
    elif choice == '2':
        index = int(input("Enter the index of the entry to display: "))
        if 0 <= index < len(df):
            print(df.iloc[index])
        else:
            print("Invalid index!")

def choose_csv(directory):
    # List all files in the specified directory
    files = os.listdir(directory)
    csv_files = [f for f in files if f.endswith('.csv')]
    
    # Display files for user selection
    if len(csv_files) == 0:
        print("No CSV files found in the specified directory.")
        return None

    print("\nPlease choose a CSV file:")
    for index, file in enumerate(csv_files):
        print(f"{index}: {file}")

    choice = int(input("Enter your choice (number): "))
    # Handle the input
    if 0 <= choice < len(csv_files):
        return os.path.join(directory, csv_files[choice])
    else:
        print("Invalid choice.")
        return None

def main():
    # Prompt user to provide a directory path if needed or you can take it from args or direct assignment
    csv_path = choose_csv('./data/output/')
    if csv_path is not None:
        results_df = load_results(csv_path)
        display_report(results_df)

if __name__ == "__main__":
    main()