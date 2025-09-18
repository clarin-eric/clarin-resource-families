import json
import os

def merge_json_files(directory_path, output_file):
    merged_data = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            with open(os.path.join(directory_path, filename), 'r') as file:
                data = json.load(file)
                new_data = process_input(data)
                merged_data.append(data)
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


# print(d)

start_path = "../corpora"
for filename in os.listdir(start_path):
    directory_path = "../corpora/" + filename
    print(f"Processing family '{directory_path}'")
    output_file = "../export/" + filename + ".json"
    merge_json_files(directory_path, output_file)
    print(f"Merged data written to '{output_file}'")


