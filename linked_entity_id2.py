import os 
import csv

def load_csv_mapping(csv_path):
    #Load the CSV file and return a dictionary mapping Content Version Id to Linked Entity Id.
    mapping = {}#empty dictionary
    with open(csv_path, mode='r', encoding='utf-8') as csv_file:#opening a csv file as a csv file and reading it, encoding it as well
        reader = csv.DictReader(csv_file)#reading csv file and maps into a dictionary
        for row in reader:#loops over each row in the csv file
            #extracting and accessing values in the rows
            content_version_id = row['Content Version Id']
            linked_entity_id = row['Linked Entity Id']
            extension_type = row['Extension Type']
            #mapping each content id to the linked id and the extension
            #will be populated as: "xxx": ("xxx", "xxx")
            mapping[content_version_id] = (linked_entity_id, extension_type)
    return mapping

def rename_files_in_folder(folder_path, csv_path):
    """Rename files in the folder based on the mapping provided by the CSV."""
    mapping = load_csv_mapping(csv_path)
    seen_links = {}#creating a dictionary for already seen links
    
    for filename in os.listdir(folder_path):#looping through the files in the directory
        file_path = os.path.join(folder_path, filename)#creating a join path for the files
        if os.path.isfile(file_path):#chenking to see if the files is a file
            # Check if the file name (without extension) matches any Content Version Id in the mapping
            name, _ = os.path.splitext(filename)#splitting the filename from the extension
            if name in mapping:#if the name of the file is in the mapping dictionary
                #extracting the linked ID and the extension from the mapping dictionary
                #mapping[name] gives ("linked id", "extension")
                linked_entity_id, new_extension = mapping[name]

                #Handle duplicates by appending a number 
                if linked_entity_id in seen_links:
                    seen_links[linked_entity_id] += 1#increment count in seen links by 1
                    #seen_links[linked_entity_id] is the count
                    new_name = f"{linked_entity_id}_{seen_links[linked_entity_id]}.{new_extension}"
                else:
                    #added the linked_entity_id to the seen_links dictionary
                    seen_links[linked_entity_id] = 1#initialize count to 1
                    new_name = f"{linked_entity_id}.{new_extension}"
                #new_path = os.path.join(folder_path, new_name)
                #os.rename(file_path, new_path)
                print(f"Renamed: {filename} -> {new_name}")

if __name__ == '__main__':
    folder_path = "C:/Users/rjbri/OneDrive/Python/Intern/large_test_folder"
    csv_path = "entity_id.csv"
    rename_files_in_folder(folder_path, csv_path)

        