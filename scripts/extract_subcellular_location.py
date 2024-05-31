import requests

def get_subcellular_location(uniprot_id):
    # make http request to uniprot
    url = f'https://www.ebi.ac.uk/proteins/api/proteins/{uniprot_id}'
    response = requests.get(url, headers={'Accept': 'application/json'})

    if response.ok:
        data = response.json()
        # Check if 'comments' key exists and if it's a list
        if 'comments' in data and isinstance(data['comments'], list):
            subcellular_locations = [comment.get('subcellular location') for comment in data['comments']]
            print(subcellular_locations)
            return subcellular_locations
        else:
            print(f"No subcellular location information found for {uniprot_id}")
            return None
    else:
        print(f"Error retrieving data for UniProt ID: {uniprot_id}")
        return None

if __name__ == "__main__":
    print("Hello World")

    uniprot_ids = ['P62983']

    for uniprot_id in uniprot_ids:
        get_subcellular_location(uniprot_id)