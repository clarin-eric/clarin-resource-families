import json
import os

def merge_json_files(directory_path, output_file, process_flag):
    merged_data = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            print(f"Filename: '{filename}'")
            with open(os.path.join(directory_path, filename), 'r') as file:
                data = json.load(file)
                if (process_flag):
                    new_data = process_input(data)
                merged_data.append(data)
    print(f"Output: '{output_file}'")
    with open(output_file, 'w') as outfile:
        json.dump(merged_data, outfile)

# read in list of language codes
d = {}
with open('lang-codes.csv') as f:
  d = dict(x.rstrip().split(',', 1) for x in f)

# process JSON before merging
def process_input(data):
    langs = data['Language']
    for index, value in enumerate(langs):
        if value in d.keys():
            langs[index] = d[value]
    return data

def merge_all():
    complete_output_file = "../export/all_crf_items.json"
    merged_data = []
    print("Creating complete merged JSON")
    for filename in os.listdir(export_path):        
        with open(os.path.join(export_path, filename), 'r') as file:
            data = json.load(file)
            merged_data.append(data)
    with open(complete_output_file, 'w') as outfile:
        json.dump(merged_data, outfile)




# print(d)

start_path = "../corpora/"
export_path = "../export/corpora/"
for filename in os.listdir(start_path):
    directory_path = os.path.join(start_path, filename)
    print(f"Processing family '{directory_path}'")
    output_file = export_path + filename + ".json"
    merge_json_files(directory_path, output_file, True)
    print(f"Merged data written to '{output_file}'")
merge_all()




