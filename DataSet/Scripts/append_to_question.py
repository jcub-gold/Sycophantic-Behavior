import os
import json

def add_to_question(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.json'):
                json_path = os.path.join(root, file)
                with open(json_path, 'r') as f:
                    data = json.load(f)
                data['general_inquiry']['question'] = 'Just give me the final answer!!! ' + data['general_inquiry']['question']
                with open(json_path, 'w') as f:
                    json.dump(data, f, indent=4)

if __name__ == "__main__":
    dataset_dir = 'DataSet\json_files'
    add_to_question(dataset_dir)