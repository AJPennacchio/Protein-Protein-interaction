import requests

def fetch_protein_sequence(protein_id):
    url = f"https://www.uniprot.org/uniprot/{protein_id}.fasta"
    response = requests.get(url)
    if response.ok:
        return response.text.split('\n', 1)[-1]  # Exclude the UniProt ID from the sequence header
    else:
        response.raise_for_status()

def create_protein_database(protein_ids, output_file):
    with open(output_file, "w") as fasta_file:
        for protein_id in protein_ids:
            try:
                sequence = fetch_protein_sequence(protein_id.strip())
                if sequence:
                    fasta_file.write(f">{protein_id.strip()}\n{sequence}\n")
            except Exception as e:
                print(f"Failed to fetch sequence for protein ID {protein_id}: {e}")

# Example usage:
protein_ids_file = "../data/receptors.txt"  # Path to the text file containing protein IDs
output_file = "../data/database.fasta"  # Path to the output FASTA file

with open(protein_ids_file, "r") as f:
    protein_ids = f.readlines()

create_protein_database(protein_ids, output_file)

