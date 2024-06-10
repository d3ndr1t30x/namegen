import random
import argparse

def print_ascii_art():
    art = """
 _______                          ________                  __________        
 \      \ _____    _____   ____  /  _____/  ____   ____     \______   \___.__.
 /   |   \\__  \  /     \_/ __ \/   \  ____/ __ \ /    \     |     ___<   |  |
/    |    \/ __ \|  Y Y  \  ___/\    \_\  \  ___/|   |  \    |    |    \___  |
\____|__  (____  /__|_|  /\___  >\______  /\___  >___|  / /\ |____|    / ____|
        \/     \/      \/     \/        \/     \/     \/  \/           \/     
                                                   """
    print(art)

def load_names(filename):
    """Load names from a text file into a list."""
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit(1)

def generate_names(first_names, last_names, count, case_flag):
    """Generate a list of random names from first and last names."""
    names = []
    for _ in range(count):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        
        if case_flag == 'normal':
            name = f"{first_name.capitalize()} {last_name.capitalize()}"
        elif case_flag == 'caps':
            name = f"{first_name.upper()} {last_name.upper()}"
        
        names.append(name)
    return names

def save_names(names, filename):
    """Save the generated names to a text file."""
    with open(filename, 'w') as file:
        for name in names:
            file.write(name + '\n')

def main():
    print_ascii_art()
    
    parser = argparse.ArgumentParser(description="Generate random names for sock puppet accounts.")
    parser.add_argument('first_names_file', type=str, help="Path to the file containing first names")
    parser.add_argument('last_names_file', type=str, help="Path to the file containing last names")
    parser.add_argument('output_file', type=str, help="Path to the output file where generated names will be saved")
    parser.add_argument('-n', '--number', type=int, default=100, help="Number of names to generate (default: 100)")
    parser.add_argument('--case', type=str, choices=['normal', 'caps'], default='normal', 
                        help="Specify the case of the output names: 'normal' for capitalized, 'caps' for uppercase (default: normal)")

    args = parser.parse_args()

    first_names = load_names(args.first_names_file)
    last_names = load_names(args.last_names_file)
    
    names = generate_names(first_names, last_names, args.number, args.case)
    
    save_names(names, args.output_file)
    
    print(f"{args.number} names generated and saved to '{args.output_file}' in '{args.case}' case.")

if __name__ == "__main__":
    main()
