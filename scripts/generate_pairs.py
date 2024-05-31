with open('../data/receptors.txt', 'r') as file1:
    proteins1 = file1.read().splitlines()

# Read proteins from the second text file
with open('../data/ligands.txt', 'r') as file2:
    proteins2 = file2.read().splitlines()

# Open a new TSV file to write the protein pairs
with open('protein_pairs.tsv', 'w') as tsvfile:
    # Iterate over each protein pair combination
    for protein1 in proteins1:
        for protein2 in proteins2:
            # Write the protein pair to the TSV file
            tsvfile.write(f"{protein1}\t{protein2}\n")
