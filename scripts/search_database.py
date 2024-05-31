def read_proteins_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def find_missing_proteins(proteins, search_filename):
    found_proteins = set()
    with open(search_filename, 'r') as file:
        for line in file:
            for protein in proteins:
                if protein in line:
                    found_proteins.add(protein)
    return list(set(proteins) - found_proteins)

def main():
    proteins_file = "../data/receptors.txt"
    search_file = "../data/database.fasta"

    proteins = read_proteins_from_file(proteins_file)
    missing_proteins = find_missing_proteins(proteins, search_file)

    print("Proteins not found in the search file:")
    for protein in missing_proteins:
        print(protein)

if __name__ == "__main__":
    main()

